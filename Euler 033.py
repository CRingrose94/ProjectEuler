def compute():

    fraction_product = 1

    for x in range(1, 9):
        for y in range(1, 9):
            small_fraction = x / y
            if small_fraction < 1:
                for i in range(1, 10):
                    numerator = float(str(x) + str(i))
                    denominator = float(str(i) + str(y))
                    larger_fraction = numerator / denominator
                    if larger_fraction == small_fraction:
                        fraction_product *= small_fraction
    return fraction_product


if __name__ == '__main__':

    print(compute())
