from datetime import date


def compute():

    for y in range(1901, 2001):
        for m in range(1, 13):
            if date(y, m, 1).weekday() == 6:
                yield 1


if __name__ == '__main__':

    print(sum(compute()))
