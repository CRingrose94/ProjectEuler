def pandigital_check(x, y):

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    concat = str(x) + str(y) + str(x * y)

    return all(x in concat for x in numbers) and (len(concat) == 9)


def yield_pandigital_products(limit):

    for x in range(1, (limit // 200)):
        for y in range(1, limit):
            if pandigital_check(x, y):
                yield x * y


def compute(limit):

    return sum(set(yield_pandigital_products(limit)))


if __name__ == '__main__':

    print(compute(10000))
