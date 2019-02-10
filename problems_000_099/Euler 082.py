test_matrix = [[131, 673, 234, 103, 18],
               [201, 96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524, 37, 331]]


def read_file():
    """returns list of lists (2d array) of numbers in the matrix text file"""
    with open("../euler_files/p082_matrix.txt") as file:

        return [list(map(int, line.strip().split(","))) for line in file]


def compute():
    """Starts on left side of matrix. Three loops for each valid direction (up, down, right)
    Generates list of lists of possible path sums as you move through the matrix [a, a+b, a+b+c ...]
    The minimum path-sum is therefore the smallest final value from these lists.
    """

    matrix = read_file()

    # seeds starting values from left column
    opt = [[row[0]] for row in matrix]

    for col in range(1, len(matrix[0])):
        for row in range(len(matrix)):
            opt[row].append(matrix[row][col] + opt[row][col - 1])

        for row in range(1, len(matrix)):
            if opt[row - 1][col] + matrix[row][col] < opt[row][col]:
                opt[row][col] = opt[row - 1][col] + matrix[row][col]

        for row in reversed(range(len(matrix) - 1)):
            if opt[row + 1][col] + matrix[row][col] < opt[row][col]:
                opt[row][col] = opt[row + 1][col] + matrix[row][col]

    return min(row[-1] for row in opt)


if __name__ == '__main__':

    print(compute())
