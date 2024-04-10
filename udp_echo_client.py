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
    pass  # delete this and write your code


def create_socket(timeout: int) -> socket.socket:
    """Create IPv4 UDP client socket"""
    pass  # delete this and write your code
    # Set socket timeout here.


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
    pass  # delete this and write your code


def main() -> None:
    SERVER_HOSTNAME, SERVER_PORT, NUM_PINGS, TIMEOUT = parse_args()
    # Get IP from hostname
    SERVER_IP = socket.gethostbyname(SERVER_HOSTNAME)
    # Create the socket
    client_socket = create_socket(timeout=TIMEOUT)

    pass  # delete this and write your code
    # Note: you will want exception handling for lost packets (think timeout).
    # round RTT the nearest 10ms before adding it to rtt_hist and displaying it

    # ping stats
    loss, rtt_min, rtt_avg, rtt_max, rtt_mdev = net_stats(
        num_pings=NUM_PINGS, rtt_hist=rtt_hist
    )
    pass  # delete this and write your code


if __name__ == "__main__":
    main()
