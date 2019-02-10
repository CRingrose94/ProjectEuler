def combs(lower, upper):

    return len(set(i ** j for i in range(lower, upper + 1) for j in range(lower, upper + 1)))


if __name__ == '__main__':

    print(combs(2, 100))
