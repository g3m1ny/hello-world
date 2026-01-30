#!/usr/bin/env python3
"""
A simple Hello World program in Python
"""

from datetime import datetime


def main():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, World! Current date and time: {timestamp}")

if __name__ == "__main__":
    main()
