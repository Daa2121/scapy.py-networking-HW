#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
UDP_echo program
Solution using scapy
Solution
"""
import time
import sys
import statistics
import socket  # Delete this line and don't use socket...
from scapy.all import *  # type: ignore

# https://scapy.readthedocs.io/en/latest/troubleshooting.html
conf.L3socket = L3RawSocket  # type: ignore
# sometimes needed for default gateway, and
# always for localhost, and
# sometimes not for remote.


def parse_args() -> tuple[str, int, int, int]:
    """
    parses the 4 args:
    server_hostname, server_port, num_pings, timeout
    """
    pass #delete this and write (copy from first part)


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
    """
    pass #delete this and write (copy from first part)


def main() -> None:
    SERVER_HOSTNAME, SERVER_PORT, NUM_PINGS, TIMEOUT = parse_args()
    # Get IP from hostname
    pass #delete this and write (copy most, but not all, from first part)


if __name__ == "__main__":
    main()
