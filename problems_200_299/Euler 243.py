from helpers import prime_sieve


def compute(goal):

    primes = prime_sieve(100)

    r, d = 1, 1
    for prime in primes:
        for i in range(2, prime):
            if (r * i / float(d * i - 1)) < goal:
                return d * i
        r *= prime - 1
        d *= prime
        if (r / float(d - 1)) < goal:
            return d

    else:
        raise Exception("Increase length of prime list to obtain result.")


if __name__ == '__main__':

    resilient = 15499 / float(94744)

    print(compute(resilient))
