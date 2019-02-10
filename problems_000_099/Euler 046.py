def compute():

    n = 5
    step = 1
    prime_set = {3}

    while True:
        if all(n % p for p in prime_set):
            prime_set.add(n)
        else:
            if not any((n - 2 * i * i) in prime_set for i in range(1, n)):
                return n

        n += 3 - step
        step *= -1


if __name__ == '__main__':

    print(compute())
