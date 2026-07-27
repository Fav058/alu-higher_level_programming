#!/usr/bin/python3
"""Reads stdin line by line and computes log metrics."""
import sys
import re

LOG_PATTERN = re.compile(
    r'^\S+ - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)
VALID_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_stats(total_size, status_codes):
    """Print the accumulated file size and status code counts.

    Args:
        total_size (int): The total accumulated file size.
        status_codes (dict): A mapping of status code to count.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            match = LOG_PATTERN.match(line.strip())
            if match:
                code, size = match.groups()
                total_size += int(size)
                if code in VALID_CODES:
                    status_codes[code] = status_codes.get(code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
