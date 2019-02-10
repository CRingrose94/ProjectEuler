from helpers import prime_sieve, is_prime


def m(n, a, b):

    return n * n + a * n + b


def compute(limit):

    n_max = 0

    for b in prime_sieve(limit):
        for a in range(-b, 0, 2):
            n = 1
            while m(n, a, b) > 0 and is_prime(m(n, a, b)):
                n += 1
            if n > n_max:
                n_max, prod = n, a * b
    return prod


if __name__ == '__main__':

    print(compute(1000))
