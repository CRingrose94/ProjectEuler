from helpers import prime_sieve, is_prime


def eight_prime_family(prime, rd):
    c = 0
    for digit in '0123456789':
        n = int(str.replace(prime, rd, digit))
        if n > 100000 and is_prime(n):
            c += 1
    return c == 8


def compute(limit):

    for prime in prime_sieve(limit):
        if prime > limit // 10:
            s = str(prime)
            last_digit = s[5:6]
            if s.count('0') == 3 and eight_prime_family(s, '0'):
                return s
            if s.count('1') == 3 and last_digit != '1' and eight_prime_family(s, '1'):
                return s
            if s.count('2') == 3 and eight_prime_family(s, '2'):
                return s


if __name__ == '__main__':

    print(compute(1000000))
