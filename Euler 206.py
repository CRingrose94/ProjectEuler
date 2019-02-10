def compute():

    unique = str(1234567890)

    for i in range(10 ** 9, 5 * (10 ** 9), 10):
        j = i * i
        if str(j)[::2] == unique:
            return i


if __name__ == '__main__':

    print(compute())
