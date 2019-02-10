"""
Managed to get this one to be very fast! Could actually speed it up quite a lot by only calculating the perimeter
and not the side lengths. I think my second function is a little confusing (not very pythonic) but it runs quickly.
"""

from math import gcd, ceil
from collections import Counter


def primitive_triple_perimeters(limit):
    """Generates all primitive triples with perimeter less than limit.
    If you only need the perimeter of the triangle, you can instead use 2(m^2 + mn)
    Calculating all side lengths is just for future-proofing.
    """

    triples = set()

    for m in range(3, int(limit ** 0.5) + 1, 2):
        for n in range(m - 2, 0, -2):
            if gcd(m, n) == 1:

                a = (m * m - n * n) // 2
                b = m * n
                c = (m * m + n * n) // 2

                wire = a + b + c

                if wire <= limit:
                    triples.add(wire)

    return triples


def all_triples(limit):
    """Given all primitive triples, generates all triples with k > 0, with perimeter up to limit.
    If (a, b, c) is some primitive triple, generate all triples k(a, b, c),
    Where k is some positive integer.

    This function merely counts the number of triples, doesn't actually generate the triples themselves.
    """

    prim_peris = list(primitive_triple_perimeters(limit))
    non_prims = []

    for i in prim_peris:
        if limit % 1 == 0:
            non_prims.extend((i * j for j in range(2, limit // i + 1)))
        else:
            non_prims.extend((i * j for j in range(2, int(ceil(limit // i)))))

    count = Counter(prim_peris + non_prims)
    return sum(1 for x in count if count[x] == 1)


if __name__ == '__main__':

    print(all_triples(1500000))
