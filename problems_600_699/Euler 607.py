import math
import numpy as np
from scipy.optimize import minimize


def time_calc(x):

    p = 50 / math.sqrt(2) - 25
    h = np.array([p, 10, 10, 10, 10, 10, p])
    v = np.array([10, 9, 8, 7, 6, 5, 10])
    a = 100 / math.sqrt(2)
    res = 0

    for i in range(6):
        res += math.sqrt(h[i] ** 2 + x[i] ** 2) / v[i]
    res += math.sqrt((a - sum(x)) ** 2 + h[6] ** 2) / v[6]
    return res


def compute():
    x0 = np.array([0.01 for i in range(6)])
    res = minimize(time_calc, x0, method='nelder-mead',
                   options={'xtol': 1e-12, 'maxiter': 10000})
    return res.fun


if __name__ == '__main__':

    print(compute())
