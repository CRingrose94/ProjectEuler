from math import log


def read_file():

    with open('p099_base_exp.txt') as file:
        return [list(map(int, line.split(","))) for line in file]


def compute():

    # Cache list
    data = read_file()

    log_list = [row[1] * log(row[0]) for row in data]

    return log_list.index(max(log_list)) + 1


if __name__ == '__main__':

    print(compute())
