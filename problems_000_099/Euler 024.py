from itertools import permutations as pmt


def perm_gen(limit, pos):

    return sorted(pmt(range(limit)))[pos - 1]


if __name__ == '__main__':

    print(perm_gen(10, 1000000))
