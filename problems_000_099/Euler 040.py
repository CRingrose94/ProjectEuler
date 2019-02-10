def int_gen(limit):

    n = '0.'
    for i in range(1, limit + 1):
        n += str(i)
    return n


def dn(n):

    return int(int_gen(n)[n + 1])


def compute():

    return dn(1) * dn(10) * dn(100) * dn(1000) * dn(10000) * dn(100000) * dn(1000000)


if __name__ == '__main__':
    print(compute())
