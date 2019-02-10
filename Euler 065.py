def continued_fraction_e(n):

    if n == 0:
        return 2
    elif n % 3 == 2:
        return n // 3 * 2 + 2
    return 1


def compute():

    numer, denom = 1, 0

    for i in reversed(range(100)):
        numer, denom = continued_fraction_e(i) * numer + denom, numer

    return sum(int(j) for j in str(numer))


if __name__ == "__main__":

    print(compute())
