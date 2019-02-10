from math import gcd
from helpers import prime_sieve


def compute(limit):

    pres = []

    def rec(pi, rest, coef, pres=pres):
        ret = rest * coef
        for pj in range(pi, len(pres)):
            if pres[pj][0][0] > rest:
                break
            for p1, c1 in pres[pj]:
                if p1 > rest:
                    break
                ret += rec(pj + 1, rest // p1, coef * c1)
        return ret

    for prime in prime_sieve(int(limit ** 0.5)):
        q, prev, e = prime * prime, 1, 2
        pre = []
        while q <= limit:
            g = gcd(e * (q // prime), q)
            if g - prev:
                pre.append((q, g - prev))
            q *= prime
            e += 1
            prev = g
        pres.append(pre)
    print(rec(0, limit, 1) - 1)


if __name__ == '__main__':

    print(compute(5 * 10 ** 5))
