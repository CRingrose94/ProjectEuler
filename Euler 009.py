def compute(limit):
    """Returns the product of the lowest (or only) triplet where i + j + k = limit."""

    for i in range(limit // 2):
        for j in range(limit // 2):
            k = (i * i + j * j) ** 0.5
            if i + j + k == limit:
                return int(i * j * k)


if __name__ == '__main__':

    print(compute(1000))
