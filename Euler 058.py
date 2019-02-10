from helpers import is_prime


def diagonal_sum():

    primes = 0
    not_primes = 0

    for i in range(1, 28000):

        top_right = ((2 * i) ** 2) - (2 * i) + 1
        top_left = ((2 * i) ** 2) + 1
        bottom_right = ((2 * i) - 1) ** 2
        bottom_left = (((2 * i) + 1) ** 2) - ((2 * i) + 1) + 1

        if is_prime(top_right):
            primes += 1
        else:
            not_primes += 1
        if is_prime(top_left):
            primes += 1
        else:
            not_primes += 1
        if is_prime(bottom_right):
            primes += 1
        else:
            not_primes += 1
        if is_prime(bottom_left):
            primes += 1
        else:
            not_primes += 1

        if primes / (not_primes + primes) <= 0.1:
            return 2 * i + 1


if __name__ == '__main__':

    print(diagonal_sum())
