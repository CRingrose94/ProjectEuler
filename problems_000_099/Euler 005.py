def check_divisibility(n):
    """Check if n is divisible by all numbers up to 20.
    Being divisible by numbers 11->20 means it is implicitly divisible by numbers 1->10 too.
    """

    for divisor in range(11, 21):
        if n % divisor != 0:
            return False
    return True


def compute():
    """Calculates the smallest positive number evenly divisible by 1->20.
    The lowest common factor of {1, 2 ... 20} is 2520, so this is the increment.
    """

    x = 2520

    while not check_divisibility(x):
        x += 2520
    return x


if __name__ == '__main__':

    print(compute())
