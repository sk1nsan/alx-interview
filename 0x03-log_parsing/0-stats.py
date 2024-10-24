#!/usr/bin/python3

""" Log parsing """

import sys
import re
import signal

total_size = 0
status_code = {"200": 0,
               "301": 0,
               "400": 0,
               "401": 0,
               "403": 0,
               "404": 0,
               "405": 0,
               "500": 0}


def parse_line(line):
    """ parses the line """
    """ 2024-10-24 17:45:35.904169 """
    pattern = re.compile(r"""
    ^
    \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
    \s-\s
    \[\d+-\d+-\d+\s\d+:\d+:\d+\.\d+\]
    \s"GET\s/ projects/260\sHTTP/1\.1"
    \s(\d{1,3})
    \s(\d+)
    $
""", re.VERBOSE)
    match = pattern.search(line)
    if match:
        return match.groups()
    return None


def signal_handler(sig, frame):
    """ handles signal error """
    print(f"File size: {total_size}")
    for key, value in status_code.items():
        if value:
            print(f"{key}: {value}")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    for line in sys.stdin:
        for i in range(10):
            parsed_line = parse_line(line)
            if parsed_line:
                code, size = parsed_line
                if code not in status_code:
                    continue
                status_code[code] += 1
                total_size += int(size)
            else:
                continue
        print(f"File size: {total_size}")
        for key, value in status_code.items():
            if value:
                print(f"{key}: {value}")
