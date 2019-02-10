from math import log10
from decorators import timer_func


def log_fact(integer):

    return sum(log10(i) for i in range(1, integer + 1))


@timer_func
def combinatorics():

    count = 0

    for n in range(23, 101):
        for r in range(n):
            a, b, c = log_fact(n), log_fact(r), log_fact(n - r)
            if 10 ** (a - b - c) > 1000000:
                count += 1
    return count


if __name__ == '__main__':

    print(combinatorics())
