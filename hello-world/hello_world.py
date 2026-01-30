#!/usr/bin/env python3
"""
A simple Hello World program in Python
"""

from datetime import datetime


def main():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    # Print 'Hello' in green using ANSI escape codes
    green = "\033[32m"
    reset = "\033[0m"
    print(f"{green}Hello{reset}, World! Current date and time: {timestamp}")

if __name__ == "__main__":
    main()
