from helpers import is_pandigital


def first_digits():

    n, m = 1, 1
    poss_k1 = []
    for k in range(3, 5 * 10 ** 5):
        l = int(str(n + m)[:20])
        if is_pandigital(str(l)):
            poss_k1.append(k)
        n, m = m, l
    return poss_k1


def last_digits():

    n, m = 1, 1
    poss_k2 = []
    for k in range(3, 5 * 10 ** 5):
        l = int(str(n + m)[-10:])
        if is_pandigital(str(l)):
            poss_k2.append(k)
        n, m = m, l
    return poss_k2


def compute():

    fd = first_digits()
    ld = last_digits()
    for i in range(len(fd)):
        for j in range(len(ld)):
            if fd[i] == ld[j]:
                return fd[i]


if __name__ == '__main__':

    print(compute())

# [24347, 78826, 182156, 243747, 309998, 329468, 344549]
# Using calculator, 329468 is correct.
# first_digits - for whatever reason - is giving the wrong answer.
