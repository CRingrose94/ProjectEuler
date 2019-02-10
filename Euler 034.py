from math import factorial as fact


def compute():

    curious = []
    total = 0

    for i in range(3, 1000000):
        s = sum(fact(int(digit)) for digit in str(i))
        if s == i:
            curious.append(i)
            total += i

    return total


if __name__ == '__main__':

    print(compute())
