from math import factorial


def compute(iterations):

    # Calculate desired number of coefficients; store as empty list, p.
    win_limit = (iterations - 1) // 2
    coeff = [1] + [0] * win_limit
    for i in range(iterations + 1):
        for j in range(win_limit, 0, -1):
            coeff[j] += i * coeff[j - 1]

    return int(factorial(iterations + 1) / sum(coeff))


if __name__ == '__main__':

    print(compute(15))
