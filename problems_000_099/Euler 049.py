from helpers import prime_sieve
from decorators import timer_func


@timer_func
def find_perms(limit):

    primes = prime_sieve(limit)
    ans = []

    for i in primes:
        for j in range(1000, limit // 3):
            if i + j in primes and i + 2 * j in primes and sorted(str(i)) == sorted(str(i + j)) == sorted(str(i + 2 * j)):
                ans.append((i, i + j, i + 2 * j))
    return ans


if __name__ == '__main__':

    print(find_perms(10000))
