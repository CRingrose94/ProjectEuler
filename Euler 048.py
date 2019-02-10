def compute(limit):

    return str(sum(i ** i for i in range(1, limit + 1)))[-10:]


if __name__ == '__main__':

    print(compute(1000))
