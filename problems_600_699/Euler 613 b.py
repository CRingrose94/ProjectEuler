"""
For some reason, scipy doesn't integrate precisely enough for this answer so I did it by hand. Not too bad in the end.
See forum post for method.
"""

import scipy.integrate as integ
from numpy import pi, arctan


def integrand(x, y):

    alpha = arctan(y / (3 - x)) + arctan(x / (4 - y)) + pi / 2

    return alpha / (12 * pi)


def x_bounds():

    return [0, 4]


def y_bounds(x):

    return [0, 3 - 0.75 * x]


if __name__ == '__main__':

    abs_error = {"epsabs": 10 ** (-10)}
    rel_error = {"epsrel": 10 ** (-10)}
    limit = {"limit": 100000000000}

    ans, err, neval = integ.nquad(integrand, [y_bounds, x_bounds], opts=[abs_error, rel_error], full_output=True)

    print("The probability is: {}, with error: {}. The number of evaluations was {}".format(ans, err, neval["neval"]))

    print("The answer is therefore between: {:.10f} and {:.10f}".format(ans - err, ans + err))

# 0.3916721504
