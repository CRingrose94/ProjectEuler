from helpers import prime_sieve


def compute(limit):

    return sum(prime_sieve(limit + 1))


if __name__ == '__main__':

    print(compute(2 * 10 ** 6))
