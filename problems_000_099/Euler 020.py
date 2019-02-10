from math import factorial


def compute(limit):

    return sum(int(i) for i in str(factorial(limit)))


if __name__ == '__main__':

    print(compute(100))
