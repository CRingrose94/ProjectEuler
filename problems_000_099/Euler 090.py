"""
You can completely ignore the number 7 for construction.
However, it can be used to add possibilities if you have a free side left over.
6 and 9 are equivalent and so there's no need to check both.
By setting 9 to 6, 49 and 64 become the same i.e. if you get one, you automatically get the other.
With neither 7 nor 9 required, you only need 8 of the digits to be represented across 2 dice.
This means 8 of the 12 available spaces have to be '01234568' but the rest can be whatever.
Which numbers go on which die is also important however.
"""

from itertools import combinations


def compute():

    squares = [[0, 1], [0, 4], [0, 6], [1, 6], [2, 5], [3, 6], [4, 6], [8, 1]]
    count = 0

    for cube_1 in combinations(list(range(9)) + [6], 6):
        for cube_2 in combinations(list(range(9)) + [6], 6):
            for square in squares:
                if not (square[0] in cube_1 and square[1] in cube_2) and not (
                        square[0] in cube_2 and square[1] in cube_1):
                    break
            else:
                count += 1
    return count // 2


if __name__ == '__main__':

    print(compute())
