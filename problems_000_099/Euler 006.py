def sum_of_squares(limit):
    """Returns the sum of all squared integers up to limit."""

    return sum(i ** 2 for i in range(limit + 1))


def square_of_sum(limit):
    """Returns the square of the sum of all integers up to limit."""

    return sum(i for i in range(limit + 1)) ** 2


def compute(limit):

    return square_of_sum(limit) - sum_of_squares(limit)


if __name__ == '__main__':

    print(compute(100))
