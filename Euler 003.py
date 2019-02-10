def is_prime(n):
    """Basic prime checker. Checks if n is prime by checking divisors up to sqrt(n)."""

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def compute(x):
    """Finds the largest prime factor of a number, x."""

    for divisor in reversed(range(2, int((x + 1) ** 0.5))):
        if is_prime(divisor) and x % divisor == 0:
            return divisor


if __name__ == '__main__':

    print(compute(600851475143))
