def compute(side_len):
    """Computes the number of 'Manhattan routes' through a grid of size side_len ** 2.
    The Manhattan routes would be the set of shortest purely horizontal/vertical routes.

    Surely there's an analytical method for this?
    """

    grid = [1] * side_len
    for i in range(side_len):
        for j in range(i):
            grid[j] += grid[j - 1]
        grid[i] = 2 * grid[i - 1]
    return grid[side_len - 1]


if __name__ == '__main__':

    print(compute(20))
