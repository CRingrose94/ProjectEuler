def compute(limit):

    n_list = range(1, limit)
    ways = [1] + [0] * limit

    for n in n_list:
        for i in range(n, limit + 1):
            ways[i] += ways[i - n]
    return ways[limit]


if __name__ == '__main__':

    print(compute(100))


'''
Alternatively *Groan*:

from sympy import npartitions


print(npartitions(100) - 1)


Alternatively 2:

There's a formula for the number of partitions which can be found on oeis.org. They even give Maple code.

'''