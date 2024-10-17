#!/usr/bin/python3
""" Minimum Operations """


def prime_decomp(n):
    """ returns the prime decomposition of n """
    primes = {}
    while (n != 1):
        for i in range(2, n + 1):
            if (not n % i):
                if i not in primes.keys():
                    primes[i] = 1
                else:
                    primes[i] += 1
                n = int(n / i)
                break
    return primes


def minOperations(n):
    """ calculate Minimum Operations """
    result = 0
    if n <= 0:
        return result
    primes = prime_decomp(n)
    for prime in primes:
        result += primes[prime] * prime
    return result
