def compute():

    pents = set()
    i = 1000

    while True:
        i += 1
        s = (3 * i * i - i) // 2
        for p_j in pents:
            if s - p_j in pents and s - 2 * p_j in pents:
                return s - 2 * p_j
        pents.add(s)


if __name__ == '__main__':

    print(compute())
