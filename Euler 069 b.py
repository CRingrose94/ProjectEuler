"""
Instead of finding all coprimes for all numbers up to a limit, analyse Euler's totient function.
This is done by multiplying the first primes together until you reach the limit (10 ** 6 in this case).
i.e.
2 x 3 x 5 x 7 x 11 ... < 10 ** 6

This problem would be very difficult if you didn't look at the Euler totient function.
Looking at the totient function makes it trivial, doable on paper even.
"""

from helpers import prime_sieve


def compute(limit):

    primes = prime_sieve(20)

    current_max_n = 1
    for p in primes:
        if current_max_n * p > limit:
            return current_max_n
        else:
            current_max_n *= p
    return current_max_n


if __name__ == '__main__':

    print(compute(1000000))
