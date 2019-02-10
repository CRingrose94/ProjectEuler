from itertools import permutations


def properties(n):

    divisors = [2, 3, 5, 7, 11, 13, 17]

    for i in range(len(divisors)):
        if int(n[i + 1:i + 4]) % divisors[i] != 0:
            return False
    return True


def compute():

    total = 0

    for j in permutations([str(x) for x in range(10)]):
        pan = ''.join(j)
        if properties(pan):
            total += int(pan)
    return total


if __name__ == '__main__':

    print(compute())
