#!/usr/bin/env python3
"""Script for calculate wildcard address(ipv4)"""
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("usage: python3 wildcard.py \"255.255.255.0\"")
        exit()

    ip_address = sys.argv[1].split('.')
    wildcard_address = [int(i) ^ 255 for i in ip_address]
    result = '.'.join([str(i) for i in wildcard_address])
    print(result)
