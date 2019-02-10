from helpers import is_prime


def rotate(m, n):

    c = 0
    while n != c:
        end = m[1:]
        end.append(m[0])
        whole = ''.join(end)
        c = int(whole)
        if not is_prime(c):
            return False
        m = list(str(whole))
    return True


def yield_circ_primes(limit):

    for i in range(3, limit):
        if is_prime(i):
            m = list(str(i))
            if rotate(m, i):
                yield i


def compute(limit):

    # (+ 1 because 2 is missed off)
    return len(list(yield_circ_primes(limit))) + 1


if __name__ == '__main__':

    print(compute(10 ** 6))
