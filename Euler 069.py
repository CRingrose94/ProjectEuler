"""
for all numbers up to n:
find number of coprimes
calculate n / number of coprimes == n / phi
"""

from math import gcd


def phi(n):

    amount = 0

    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            amount += 1

    return amount


def compute(limit):

    current_max_n = 6
    current_max_frac = 3

    for n in range(2, limit + 1, 2):    # Count up in twos as odd numbers will have more relative primes
        frac = n / phi(n)
        if frac > current_max_frac:
            current_max_n = n

    return current_max_n


if __name__ == '__main__':

    print(compute(10000))

# Too naive a method. Need to analyse Euler's totient function properly, as shown in attempt b.
