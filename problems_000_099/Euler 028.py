def compute(limit):

    total = -3
    x = (limit + 1) // 2 + 1

    for n in range(1, x):
        total += (2 * n * (2 * n - 5) + 7)
        total += ((2 * n - 2) ** 2 + 1)
        total += (2 * n * (2 * n - 3) + 3)
        total += ((2 * n - 1) ** 2)

    return total


if __name__ == '__main__':

    print(compute(1001))
