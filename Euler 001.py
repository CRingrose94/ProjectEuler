def compute(limit):
    """Calculates the sum of all multiples of 3 or 5 up to a limit."""

    return sum(i for i in range(1, limit) if i % 3 == 0 or i % 5 == 0)


if __name__ == '__main__':

    print(compute(1000))
