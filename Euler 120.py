def generate_n(a):

    return max(((a - 1) ** n + (a + 1) ** n) % (a ** 2) for n in range(1, 10 + 2 * a))


def compute():

    return sum(generate_n(a) for a in range(3, 1001))


if __name__ == '__main__':

    print(compute())
