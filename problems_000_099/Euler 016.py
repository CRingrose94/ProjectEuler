def compute(number):
    """Returns the sum of the digits of a number"""

    return sum(int(digit) for digit in str(number))


if __name__ == '__main__':

    print(compute(2 ** 1000))
