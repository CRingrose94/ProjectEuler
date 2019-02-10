from helpers import is_prime


def truncate_left(n):

    if not is_prime(n):
        return False
    else:
        i = str(n)
        while len(i) != 1:
            i = int(i[1:])
            if not is_prime(i):
                return False
            else:
                i = str(i)
                if len(i) == 1:
                    return True


def truncate_right(n):

    j = str(n)
    while len(j) != 1:
        j = int(j[:-1])
        if not is_prime(j):
            return False
        else:
            j = str(j)
            if len(j) == 1:
                return True
    else:
        return False


def compute(limit):

    for k in range(limit):
        if is_prime(k) and truncate_left(k) and truncate_right(k):
            yield k


if __name__ == '__main__':

    print(sum(compute(10 ** 6)))
