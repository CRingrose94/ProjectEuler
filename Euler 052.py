from itertools import count


def compute(limit):

    for i in count(1):
        digits = sorted(str(i))
        if all(sorted(str(i * j)) == digits for j in range(2, limit + 1)):
            return str(i)


if __name__ == '__main__':

    print(compute(6))
