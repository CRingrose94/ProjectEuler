from math import log10 as log


# (2 * 2) (6 * 6) (10 * 10) (14 * 14)
# -----------------------------------   ~= root 2
# (1 * 3) (5 * 7)  (9 * 11) (13 * 15)


def compute(limit):

    numer, denom = 3, 2

    for n in range(2, limit + 1):
        numer, denom = numer + 2 * denom, numer + denom
        if int(log(numer)) > int(log(denom)):
            yield 1


if __name__ == '__main__':

    print(sum(compute(1000)))
