#!/usr/bin/python3

""" UTF-8 Validation """


def validUTF8(data):
    """ UTF-8 Validation """
    bytes_remaining = 0
    for byte in data:
        if bytes_remaining:
            if byte & 192 != 128:
                return False
            bytes_remaining -= 1
        if not byte & 128:
            continue
        if byte & 224 == 192:
            bytes_remaining = 1
            continue
        if byte & 240 == 242:
            bytes_remaining = 2
            continue
        if byte & 248 == 240:
            bytes_remaining = 3
            continue
        return False
    return True
