"""
Jesus pooh, that's not honey; you're eating recursion!
"""

from decorators import memoise


@memoise
def compute(x):
    if x == 0:
        return 1
    if x % 2 == 1:
        return compute((x - 1) // 2)
    return compute(x // 2) + compute(x // 2 - 1)


if __name__ == '__main__':

    print(compute(10 ** 25))
