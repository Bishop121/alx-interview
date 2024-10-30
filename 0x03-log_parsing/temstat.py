#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:"""

import re
import signal
import sys
"""
    the re module for regular expression
    the signal for control + C signal.SIGINT
    sys.stdin used from sys to read standard input
"""


def signal_handler(sig, frame):
    """
        a signal handling function that get used by
        signal.signal(signal.SIGINT, signal_handler)
    """
    print_metrics(total_size, stat_count)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

"""initializing variables needed"""
total_size = 0
stat_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}  # nopep8
line_count = 0

"""
    regular expression to match the input format
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
                    <status code> <file size>
"""

log_pattern = (
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)


"""pinter helper"""


def print_metrics(total_size, stat_count):
    print(f"File size: {total_size}")
    for code in sorted(stat_count.keys()):
        count = stat_count[code]
        if count > 0:
            print(f"{code}: {count}")


"""processing the input"""
try:
    for line in sys.stdin:
        """ get each line comming from the command line or input"""
        line = line.strip()
        match = re.fullmatch(log_pattern, line)
        """
            log pattern is the regular expression
            line === string: passed
        """
        if match:
            line_count += 1
            status_code = match.group(3)
            file_size = int(match.group(4))

            total_size += file_size

            if status_code in stat_count:
                stat_count[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, stat_count)

finally:
    print_metrics(total_size, stat_count)
