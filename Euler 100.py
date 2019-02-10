"""
Abuse the fact that ratios can just be multiplied up to an arbitrarily large number.
Seems a little cheap but hey.
"""


def compute(minimum):

    b_0, n_0 = 15, 21

    while n_0 < minimum:

        b_1 = 3 * b_0 + 2 * n_0 - 2
        n_1 = 4 * b_0 + 3 * n_0 - 3

        b_0, n_0 = b_1, n_1

    return b_0


if __name__ == '__main__':

    print(compute(10 ** 12))
