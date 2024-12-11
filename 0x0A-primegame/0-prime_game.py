#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """returns the winner of the game"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primes = [n for n in range(1, num + 1) if is_prime(n)]
        if not primes:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while True:
            if not primes:
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primes.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

        isMariaTurns = not isMariaTurns

    if mariaWinsCount > benWinsCount:
        return "Maria"

    if mariaWinsCount < benWinsCount:
        return "Ben"

    return None


def is_prime(n):
    """return True if prime False otherwise"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
