from helpers import is_prime


def compute(x):
    """Finds the largest prime factor of a number, x."""

    for divisor in reversed(range(2, int((x + 1) ** 0.5))):
        if is_prime(divisor) and x % divisor == 0:
            return divisor


if __name__ == '__main__':

    print(compute(600851475143))
