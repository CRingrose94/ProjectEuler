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
        limit = j ** 0.5
        for p in primes:
            if p > limit:
                primes.append(j)
                break
            if j % p == 0:
                break
    return primes


def is_prime(n):

    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def is_palindrome(integer):

    return str(integer) == str(integer)[::-1]


def is_pandigital(concat):

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if all(x in concat for x in numbers) and (len(concat) == 9):
        return True
    return False


def sum_divisors(n):

    return sum(i for i in range(1, n) if n % i == 0)
