from helpers import is_pandigital


def compute():

    valid_pandigitals = []

    for x in range(1, 10):
        concat = str(x) + str(x * 2) + str(x * 3) + str(x * 4) + str(x * 5)
        if is_pandigital(concat):
            valid_pandigitals.append(concat)

    for x in range(10, 100):
        concat = str(x) + str(x * 2) + str(x * 3) + str(x * 4)
        if is_pandigital(concat):
            valid_pandigitals.append(concat)

    for x in range(100, 1000):
        concat = str(x) + str(x * 2) + str(x * 3)
        if is_pandigital(concat):
            valid_pandigitals.append(concat)

    for x in range(1000, 10000):
        concat = str(x) + str(x * 2)
        if is_pandigital(concat):
            valid_pandigitals.append(concat)

    return max(valid_pandigitals)


if __name__ == '__main__':

    print(compute())
