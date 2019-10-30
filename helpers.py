from math import sqrt


def prime_sieve(limit):
    """Reasonably fast prime sieve for returning all primes below <limit> as a list."""

    new_limit = (limit - 1) // 2
    boolean_list = [True] * new_limit

    for i in range(1, int(((2 * limit + 1) ** 0.5 - 1) / 2) + 1):
        start = 2 * i + 2 * i * i
        for j in range(start, new_limit + 1, 2 * i + 1):
            boolean_list[j - 1] = False
            j += 1
    primes = [2]

    for i in range(new_limit):
        if boolean_list[i]:
            primes.append(i * 2 + 3)

    return primes


def get_n_primes(n):
    """Gets the first <n> primes and returns them as a list."""
    primes = [2, 3]
    j = 3
    while len(primes) < n:
        j += 2
        limit = sqrt(j)
        for p in primes:
            if p > limit:
                primes.append(j)
                break
            if not j % p:
                break
    return primes


def is_prime(n):

    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if not n % i:
                return False
        return True


def is_palindrome(integer):

    return str(integer) == str(integer)[::-1]


def is_pandigital(concat):

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    return all(x in concat for x in numbers) and (len(concat) == 9)


def sum_divisors(n):

    return sum(i for i in range(1, n) if not n % i)
