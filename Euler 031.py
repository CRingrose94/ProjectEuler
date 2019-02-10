# coins = [1, 2, 5, 10, 20, 50, 100, 200]


def compute():

    total = 1                                           # start at one to include the £2 coin.
    for a in range(3):                                  # 0, 1 or 2 £1 coins.
        for b in range(1 + (200 - 100 * a) // 50):      # number of 50p coins depends on number of £1 coins used
            for c in range(1 + (200 - 100 * a - 50 * b) // 20):             # repeat for all coins:
                for d in range(1 + (200 - 100 * a - 50 * b - 20 * c) // 10):
                    for e in range(1 + (200 - 100 * a - 50 * b - 20 * c - 10 * d) // 5):
                        for f in range(1 + (200 - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e) // 2):
                            total += 1
    return total


if __name__ == '__main__':
    print(compute())


'''
Cannot brute force, requires dynamic programming.
Each for loop reduces the maximum total by what has been removed.
There must be a more elegant way of writing this!
'''