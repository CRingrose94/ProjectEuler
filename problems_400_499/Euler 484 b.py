from math import floor
from helpers import prime_sieve


def compute(n, p_ind=0):

    primes = prime_sieve(int(1.1 * floor(n)))
    res = n

    for p_ind in range(p_ind, len(primes)):
        p = primes[p_ind]
        pow = p ** 2

        if pow > n:
            break
        elif p == 2:
            fact = pow
        else:
            fact = p

        res += (fact - 1) * compute(n // pow, p_ind + 1)
        last = fact
        exp = 3
        pow *= p

        while pow <= n:
            if exp % p == 1:
                pow *= p
                exp += 1
            elif exp % p == 0:
                fact = p ** exp
            else:
                fact = p ** (exp - 1)

            res += (fact - last) * compute(n // pow, p_ind + 1)
            last = fact
            pow *= p
            exp += 1

    return res - 1


if __name__ == '__main__':

    print(compute(5 * 10 ** 15))
