from helpers import prime_sieve


def compute(limit):

    period = 1
    for i in prime_sieve(limit)[::-1]:               # Run through all primes backwards to find largest first
        while pow(10, period, i) != 1:          # pow(a, b ,c) == a ** b % c
            period += 1
        if i - 1 == period:
            return i


if __name__ == '__main__':
    print(compute(1000))


'''

Fermat's Little Theorem: 1/d has an n-digit cycle if 10^n - 1 % d = 0 for prime d.
1/d can have up to d - 1 repeating decimal digits.
Therefore, we need to find the largest prime number up to a limit with d - 1 digits.
This is a full reptend prime


'''