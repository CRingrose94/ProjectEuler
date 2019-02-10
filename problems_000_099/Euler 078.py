def compute(limit):

    p = {0: 1}
    n = 0

    while not p[n] % limit == 0:

        n += 1
        p[n] = 0
        k = 1
        sign = (-1) ** (k - 1)
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2

        while g1 < n + 1 or g2 < n + 1:
            if g1 < n + 1:
                p[n] += sign * p[n - g1]
            if g2 < n + 1:
                p[n] += sign * p[n - g2]

            k += 1
            sign = (-1) ** (k - 1)
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2

        if p[n] % limit == 0:

            return n, p[n]


if __name__ == '__main__':

    print(compute(10 ** 6))
