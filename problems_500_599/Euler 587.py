"""
There is a messy integral way, but why bother when this nice geometric method exists!
"""

from numpy import pi, sin, arcsin, arctan


def compute(limit):

    l_area = 1 - pi / 4

    for n in range(15, limit):
        beta = arctan(1 / n)
        gamma = arcsin((1 - 1 / n) * (sin(pi / 2 + beta)))
        alpha = pi / 2 - beta - gamma
        concave_area = 1 / (2 * n) - 0.5 * (alpha - (1 - 1 / n) * sin(alpha))
        ratio = concave_area / l_area

        if ratio <= 0.001:
            return n


if __name__ == '__main__':

    print(compute(5000))
