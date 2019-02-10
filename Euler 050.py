from decorators import timer_func
from helpers import prime_sieve


@timer_func
def consecutive_primes(prime_limit, index_max, pos_max):

    primes = prime_sieve(prime_limit)
    max_terms = 6
    max_prime = 41

    for j in range(pos_max):
        for i in range(j + index_max, j, -1):
            current_sum = sum(primes[j:i])
            if current_sum in primes and i > max_terms:
                max_terms = i
                max_prime = current_sum

    return max_prime


if __name__ == '__main__':

    print(consecutive_primes(1000000, 700, 20))
