#!/usr/bin/python3

""" Log parsing """

import sys
import re
from dateutil.parser import parse
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
    pattern = re.compile(r"""
    ^
    \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
    \s-\s
    \[(.*)\]
    \s"GET\s/ projects/260\sHTTP/1\.1"
    \s(\d{1,3})
    \s(\d+)
    $
""", re.VERBOSE)

    return pattern.search(line).groups()


def is_date(date):
    """ checkes if input is a valid date """
    try:
        parse(date, fuzzy=False)
        return True
    except ValueError:
        return False


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
                date, code, size = parsed_line
                if not is_date(date):
                    continue
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
