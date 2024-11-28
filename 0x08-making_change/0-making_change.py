#!/usr/bin/python3

"""Change comes from within"""


def makeChange(coins, total):
    """return fewest number of coins needed to meet total"""
    result = 0
    if total <= 0:
        return result
    n = len(coins)
    coins.sort()
    for i in range(n):
        j = coins[n - i - 1]
        if total >= j:
            result += total // j
            total %= j
        else:
            continue
    if total != 0:
        return -1
    return result
