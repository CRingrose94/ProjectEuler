# Consider re-writing with numpy arrays.

test_matrix = [[131, 673, 234, 103, 18],
               [201, 96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524, 37, 331]]


def read_file():
    """returns list of lists (2d array) of numbers in the matrix text file"""

    with open("p081_matrix.txt") as file:

        return [list(map(int, line.strip().split(","))) for line in file]


def compute():

    matrix = read_file()

    matrix_len = len(matrix[0])

    # Generate "sum_matrix" which is same size as "matrix", but all elements are equal to 0.
    sum_matrix = [[0 for y in range(matrix_len)] for x in range(matrix_len)]

    # Seed the last entry of "sum_matrix" with the last entry of "matrix"
    sum_matrix[matrix_len - 1][matrix_len - 1] = matrix[matrix_len - 1][matrix_len - 1]

    for i in range(matrix_len - 2, -1, -1):
        sum_matrix[matrix_len - 1][i] = matrix[matrix_len - 1][i] + sum_matrix[matrix_len - 1][i + 1]
        sum_matrix[i][matrix_len - 1] = matrix[i][matrix_len - 1] + sum_matrix[i + 1][matrix_len - 1]

    for i in range(matrix_len - 2, -1, -1):
        for j in range(matrix_len - 2, -1, -1):
            sum_matrix[i][j] = matrix[i][j] + min(sum_matrix[i][j + 1], sum_matrix[i + 1][j])

    return sum_matrix[0][0]


if __name__ == "__main__":
    print(compute())
