from helpers import prime_sieve


def compute(position):
    """Finds the positionth prime in a list of primes."""

    return prime_sieve(position * 15)[position - 1]


if __name__ == '__main__':

    print(compute(10001))
