from itertools import count
from math import sqrt, asin, pi


def compute():

    def integral(x):
        """The indefinite integral of (1 - sqrt(2x - x^2)) dx."""

        t = x - 1.0
        return t - (sqrt(1.0 - t ** 2) * t + asin(t)) / 2.0

    lsectionarea = 1.0 - pi / 4.0
    for i in count(1):
        slope = 1.0 / i
        a = slope ** 2 + 1.0
        b = -2.0 * (slope + 1.0)
        c = 1.0
        x = (2.0 * c) / (-b + sqrt(b * b - 4 * a * c))
        concavetrianglearea = x * (1.0 - sqrt((-x + 2.0) * x)) / 2.0
        concavetrianglearea += integral(1.0) - integral(x)
        if concavetrianglearea / lsectionarea < 0.001:
            return str(i)


if __name__ == "__main__":
    print(compute())
