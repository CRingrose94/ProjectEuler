"""
Given number, n:
16
sum the digits' factorials to produce new number:
1! + 6! = 721
cache results.
repeat until pattern is present in cache; while not present, add number to cache.
If pattern repeats exactly 60 times, increment count, else increase n (until n = 10 ** 6).
"""

from math import factorial as fact


# Global cache to store loops
cache = {}
# Dict of the first 10 (0-9) factorials. Known to not produce chains. Cba to memoise so it's just a global. Sue me.
fact_dict = {str(i): fact(i) for i in range(10)}


def fact_sum(n):
    """Sums the factorials of the digits."""

    return sum((fact_dict[digit] for digit in str(n)))


def fact_chain(n):
    """Extends cache as necessary."""

    if n not in cache:
        cache[n] = 1
        cache[n] += fact_chain(fact_sum(n))
    return cache[n]


def compute(limit):
    """Increments up to limit to find number of 60-length chains."""

    return sum(fact_chain(n) - 1 == 60 for n in range(limit + 1))


if __name__ == '__main__':

    print(compute(1000000))
