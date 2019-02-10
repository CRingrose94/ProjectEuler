def newton_sqrt(n):

    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2

    return x


def sum_of_digits(n):

    res = 0
    while n:
        res += n % 10
        n //= 10

    return res


def compute():

    unit = 10 ** 99
    return sum(sum_of_digits(newton_sqrt(n * unit ** 2)) for n in range(2, 100) if newton_sqrt(n) ** 2 != n)


if __name__ == '__main__':

    print(compute())
