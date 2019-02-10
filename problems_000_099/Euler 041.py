from itertools import permutations, islice
from helpers import is_prime


def compute(num_digits):

    # Option to lop off the start when using smaller pandigital numbers.
    num = '987654321'[9 - num_digits:]

    return list(islice(("".join(digit) for digit in permutations(num) if is_prime(int("".join(digit)))), 1))


if __name__ == '__main__':

    print(compute(7))
