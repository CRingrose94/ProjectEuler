from operator import itemgetter
from helpers import get_n_primes


def compute(power, modulus):

    primes = get_n_primes(power)
    count = 0
    prime_divs_list = [primes[0] ** 2]
    while True:
        j, x = min(enumerate(prime_divs_list), key=itemgetter(1))
        if x > primes[power - 1 - count]:
            break
        prime_divs_list[j] = x * x
        count += 1
        if j == len(prime_divs_list) - 1:
            prime_divs_list += [primes[len(prime_divs_list)] ** 2]
    result = 1
    for pos, prime in enumerate(primes[:-count]):
        if pos < len(prime_divs_list):
            result = (result * prime_divs_list[pos] // prime) % modulus
        else:
            result = (result * prime) % modulus
    return result


if __name__ == '__main__':

    print(compute(500500, 500500507))
