#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
UDP_echo program
Solution using python sockets
Student template
"""
import socket
import time
import sys
import statistics


def parse_args() -> tuple[str, int, int, int]:
    """
    parses the 4 args:
    server_hostname, server_port, num_pings, timeout
    """
    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])
    num_pings = int(sys.argv[3])
    timeout = int(sys.argv[4])
    return server_hostname, server_port, num_pings, timeout


def create_socket(timeout: int) -> socket.socket:
    """Create IPv4 UDP client socket"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set socket timeout here.
    client_socket.settimeout(timeout)
    return client_socket


def net_stats(
    num_pings: int, rtt_hist: list[float]
) -> tuple[float, float, float, float, float]:
    """
    Computes statistics for loss and timing.
    Mimicks the real ping's statistics.
    Check them out: `ping 127.0.0.1`
    See `man ping` for definitions.
    This is just a math function.
    Don't do any networking here.
    loss, rtt_min, rtt_avg, rtt_max, rtt_mdev
    """
    loss = (num_pings - len(rtt_hist)) / num_pings * 100 if num_pings > 0 else 0
    rtt_min = min(rtt_hist) if rtt_hist else 0
    rtt_avg = statistics.mean(rtt_hist) if rtt_hist else 0
    rtt_max = max(rtt_hist) if rtt_hist else 0
    rtt_mdev = statistics.stdev(rtt_hist) if len(rtt_hist) > 1 else 0

    return loss, rtt_min, rtt_avg, rtt_max, rtt_mdev


def main() -> None:
    SERVER_HOSTNAME, SERVER_PORT, NUM_PINGS, TIMEOUT = parse_args()
    # Get IP from hostname
    SERVER_IP = socket.gethostbyname(SERVER_HOSTNAME)
    # Create the socket
    client_socket = create_socket(timeout=TIMEOUT)

    rtt_hist = []
    received_count = 0
    total_time = 0  # Initialize total time

    print("PING localhost (127.0.0.1) 53 bytes of data.")
    for ping_num in range(1, NUM_PINGS + 1):
        message = f"PING {SERVER_HOSTNAME} ({SERVER_IP}) {ping_num} {time.asctime()}"
        start_time = time.time()
        try:
            # Send data to server
            client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
            # Receive data from server
            data, server_address = client_socket.recvfrom(1024)
            end_time = time.time()
            rtt = round((end_time - start_time) * 1000)  # round to nearest 10ms
            rtt_hist.append(rtt)
            total_time += rtt  # Add round-trip time to total time
            if data.decode()[:4] == "oops":
                print("Damaged packet")
            else:
                print(
                    f"{len(data)} bytes from {SERVER_HOSTNAME} ({SERVER_IP}): ping_seq={ping_num} time={rtt} ms"
                )
            received_count += 1
        except socket.timeout:
            print("timed out")

    # Compute packet loss percentage
    loss = ((NUM_PINGS - received_count) / NUM_PINGS) * 100

    # ping stats
    loss, rtt_min, rtt_avg, rtt_max, rtt_mdev = net_stats(
        num_pings=NUM_PINGS, rtt_hist=[rtt for rtt in rtt_hist if rtt is not None]
    )
    print(f"\n--- {SERVER_HOSTNAME} ping statistics ---")
    print(
        f"{NUM_PINGS} packets transmitted, {received_count} received, {loss:.0f}% packet loss, time {total_time}ms"
    )
    print(
        f"rtt min/avg/max/mdev = {rtt_min:.0f}/{rtt_avg:.0f}/{rtt_max:.0f}/{rtt_mdev:.0f} ms"
    )


if __name__ == "__main__":
    main()
