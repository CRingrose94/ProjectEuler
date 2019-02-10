from helpers import sum_divisors
from decorators import timer_func


def is_abundant(n):
    if sum_divisors(n) > n:
        return True
    return False


@timer_func
def compute(limit):

    abunds = [i for i in range(1, limit + 1) if is_abundant(i)]

    abund_pairs = [i + j for i in abunds for j in abunds if i + j < limit]

    # Cache set so it's not calculated every time
    abund_pairs = set(abund_pairs)
    return sum(m for m in range(1, limit) if m not in abund_pairs)


if __name__ == '__main__':

    print(compute(28124))
