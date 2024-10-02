#!/usr/bin/python3
"""
Solve Pascal's Triangle
"""


def fact(n):
    """ calculate factorial """
    if (n == 0):
        return 1
    return n * fact(n - 1)


def Combinations(n, r):
    """ return nCr """
    return int(fact(n) / (fact(n - r) * fact(r)))


def pascal_triangle(n):
    """ generate first n rows of pascal's triangle """
    final_result = []
    if n <= 0:
        return final_result
    for i in range(n):
        current_result = []
        for j in range(i + 1):
            current_result.append(Combinations(i, j))
        final_result.append(current_result)
    return final_result
