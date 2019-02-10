"""
Totient function is largest when the value it takes is prime. So you don't need to check every
number, just the primes.
An even faster method is to simply use prime pairs where n = p_1 * p_2. The totient is then:
phi = (p_1 - 1)(p_2 - 1). This is done using a list of primes up to the square root of the limit (plus some leeway)
i.e. all primes ~= sqrt(limit) or lower. So take a slightly larger number of primes (1.2* )
"""

from helpers import prime_sieve


def is_perm(x, y):

    if sorted(str(x)) == sorted(str(y)):
        return True
    return False


def compute(limit):

    primes = prime_sieve(int(1.2 * limit ** 0.5))
    del primes[:int(0.6 * len(primes))]

    min_q, min_n, i = 2, 0, 0

    for p_1 in primes:
        i += 1
        for p_2 in primes[i:]:
            n = p_1 * p_2
            if n > limit:
                return min_n
            phi = (p_1 - 1) * (p_2 - 1)
            q = n / float(phi)
            if is_perm(phi, n) and min_q > q:
                min_q, min_n = q, n


if __name__ == '__main__':

    print(compute(10 ** 7))
