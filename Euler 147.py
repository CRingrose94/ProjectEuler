def rects(m, n):

    if m < n:
        m, n = n, m
    h_and_v = m * (m + 1) * n * (n + 1) // 4
    diag = n * ((2 * m - n) * (4 * n * n - 1) - 3) // 6

    return h_and_v + diag


def compute(m, n):

    return sum(rects(i, j) for i in range(m + 1) for j in range(n + 1))


if __name__ == '__main__':
    print(compute(43, 47))
