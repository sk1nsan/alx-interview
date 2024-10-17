#!/usr/bin/python3
""" Minimum Operations """


def is_prime(n):
    """ check if a number is a prime """
    for i in range(2, int(n ** 0.5) + 1):
        if (not n % i):
            return False
    return True


def prime_decomp(n):
    """ returns the prime decomposition of n """
    primes = {}
    while (n != 1):
        for i in range(2, n + 1):
            if (is_prime(i) and not n % i):
                if i not in primes.keys():
                    primes[i] = 1
                else:
                    primes[i] += 1
                n = int(n / i)
    return primes


def minOperations(n):
    """ calculate Minimum Operations """
    primes = prime_decomp(n)
    result = 0
    for prime in primes:
        result += primes[prime] * prime
    return result
