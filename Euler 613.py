"""
Very crude brute force attempt that is basically a bad numerical integration method.
"""

from numpy import arccos, pi
from decorators import timer_func


def frange(x, y, step_size):

    x = float(x)
    x0 = x
    i = 0.0
    epsilon = step_size / 2.0
    yield x
    while x + epsilon < y:
        i += 1.0
        x = x0 + i * step_size
        yield x


@timer_func
def points_gen(step_size):

    prob, count = 0, 2

    for x in frange(step_size, 4 - step_size, step_size):
        for y in frange(0, 0.75 * (x - step_size), step_size):
            b_squared = ((4 - x) ** 2) + ((3 - y) ** 2)
            c_squared = x ** 2 + y ** 2
            b = b_squared ** 0.5
            c = c_squared ** 0.5

            ac = (b_squared + c_squared - 25)/(2 * c * b)

            alpha = arccos(ac)
            prob += alpha
            count += 1
        alpha += pi
        count += 1

    return prob / (count * 2 * pi), "count:", count


if __name__ == '__main__':

    print(points_gen(0.001))
