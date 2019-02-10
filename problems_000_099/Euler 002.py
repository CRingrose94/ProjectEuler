def compute(limit):
    """Calculates the sum of the even valued Fibonacci numbers up to a limit."""

    zero, first, next = 1, 1, 1

    count = 0
    while next <= limit:
        if next % 2 == 0:
            count += next

        next = first + zero
        zero, first = first, next
    return count


if __name__ == '__main__':

    print(compute(4000000))
