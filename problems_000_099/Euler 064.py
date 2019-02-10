# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
# Bit of a shit one here without a degree in maths.


def continued_fraction(n):

    m_n, d_n = 0.0, 1.0
    a_0 = a_n = int(n ** 0.5)
    period = 0

    if a_0 != (n ** 0.5):
        while a_n != 2 * a_0:
            m_n = d_n * a_n - m_n
            d_n = (n - m_n ** 2) / d_n
            a_n = int((a_0 + m_n) / d_n)
            period += 1
    return period


def compute(limit):

    return sum(1 for i in range(limit) if continued_fraction(i) % 2 != 0)


if __name__ == '__main__':

    print(compute(10000))
