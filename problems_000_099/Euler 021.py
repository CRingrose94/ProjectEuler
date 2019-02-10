from helpers import sum_divisors


def compute(n):

    for i in range(1, n):
        if i != sum_divisors(i) and i == sum_divisors(sum_divisors(i)):
            yield i
            

if __name__ == '__main__':

    print(sum(set(compute(10000))))
