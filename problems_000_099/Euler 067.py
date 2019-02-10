def read_file():

    tri = []

    with open("../euler_files/p067_triangle.txt") as file:
        for blob in file:
            tri.append([int(i) for i in blob.split(" ")])

    return tri


def compute():

    tri = read_file()

    for i in reversed(range(len(tri) - 1)):
        for j in range(len(tri[i])):
            tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1])

    return tri[0][0]


if __name__ == '__main__':

    print(compute())
