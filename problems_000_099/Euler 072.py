"""
This question asks for the length of the Farey sequence (-2). The length of the Farey sequence is given by
F_n = 1 + sum (from m=1 to n) phi(m) where phi is the totient function.

Original method is too slow:

import math


def totient(n):

    number = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            number += 1
    return number


def compute(limit):

    x = [totient(i) for i in range(limit + 1)]
    return sum(x) - 1


if __name__ == '__main__':

    print(compute(10 ** 6))
"""

from helpers import prime_sieve


def compute(limit):

    phi = [i for i in range(0, limit + 1)]

    primes = prime_sieve(limit)

    for p in primes:
        for j in range(1, int(limit / p) + 1):
            phi[j * p] *= (p - 1) / p
    return int(sum(phi[2:]))


if __name__ == '__main__':

    print(compute(10 ** 6))
