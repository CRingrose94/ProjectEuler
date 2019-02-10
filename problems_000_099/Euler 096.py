"""OK, yikes.
This is a messy, uncommented pit.
I'm sure there are lots of lovely algorithms for cleanly solving sudokus but this works too ... just.
"""


from decorators import timer_func


def read_file():
    """Read the file to a list where each element is a single string.
    The string is "0" if unknown or "n" if known.
    """

    with open("../euler_files/p096_sudoku.txt") as file:
        sudokus = []
        for line in file:
            if line[0] != 'G':
                for i in range(9):
                    sudokus.append(line[i])
    return sudokus


@timer_func
def final_sudoku_solution():

    ans_sum = 0
    for n in range(50):
        solved = compute(create_matrix(n))
        print(solved)
        row = solved[0][:3]
        first_three = row[0] + row[1] + row[2]
        ans_sum += int(first_three)
    return f'Final answer is: {ans_sum}.'


def create_matrix(n):

    # Create a matrix where all elements are either determined "n" or not "123456789"
    ans_matrix = [["123456789" for y in range(9)] for x in range(9)]
    sudokus = read_file()[n * 81:(n + 1) * 81]

    for i in range(9):
        for j in range(9):
            indx = i * 9 + j
            if sudokus[indx] != "0":
                ans_matrix[i][j] = sudokus[indx]
    return ans_matrix


def run_checkers(segment):
    """Run the various slice-based checkers. These all check 9 cells at once, either in squares, columns or rows."""

    segment = slice_checker(segment)
    segment = unique_checker(segment)
    segment = pair_checker(segment)
    segment = hidden_pairs(segment)

    return segment


def col_slicer(sudoku_matrix):
    """Slices a sudoku matrix into individual columns, performs some checks, then returns to the original matrix."""

    for i in range(9):
        current_col = []
        for j in range(9):
            current_col.append(sudoku_matrix[j][i])
        run_checkers(current_col)
        for j in range(9):
            sudoku_matrix[j][i] = current_col[j]

    return sudoku_matrix


def row_slicer(sudoku_matrix):
    """Slices a sudoku matrix into individual rows, performs some checks, then returns to the original matrix."""

    for row in range(9):
        current_row = []
        for col in range(9):
            current_row.append(sudoku_matrix[row][col])
        run_checkers(current_row)
        for col in range(9):
            sudoku_matrix[row][col] = current_row[col]
    return sudoku_matrix


def square_slicer(sudoku_matrix):
    """Slices a sudoku matrix into individual 9 x 9 squares, performs some checks,
    then returns to the original matrix.
    """

    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            current_square = []
            for i in range(3):
                for j in range(3):
                    current_square.append(sudoku_matrix[row + i][col + j])
            run_checkers(current_square)
            for i in range(3):
                for j in range(3):
                    sudoku_matrix[row + i][col + j] = current_square[i * 3 + j]

    return sudoku_matrix


def slice_checker(segment):

    for i in range(9):
        for j in range(9):
            if len(segment[j]) == 1 and i != j:
                temp_str = segment[i].replace(segment[j], '')
                segment[i] = temp_str
    return segment


def unique_checker(segment):

    for digit in range(1, 10):
        substr_count = 0
        for indx in range(9):
            if str(digit) in segment[indx]:
                substr_count += 1
                pos = indx
        if substr_count == 1:
            segment[pos] = str(digit)
    return segment


def pair_checker(segment):

    for i in range(9):
        pair_exists = False
        if len(segment[i]) == 2:
            first_pair = segment[i]
            pos_a = i
            for j in range(i + 1, 9):
                if segment[j] == first_pair:
                    a, b = first_pair[0], first_pair[1]
                    pos_b = j
                    pair_exists = True
                    break
            if pair_exists:
                for k in range(9):
                    if k != pos_a and k != pos_b:
                        temp_str = segment[k].replace(a, '')
                        segment[k] = temp_str
                        temp_str = segment[k].replace(b, '')
                        segment[k] = temp_str
    return segment


def pointing_pairs_cols(sudoku_matrix):

    for col in range(9):
        current_col = []
        for row in range(9):
            current_col.append(sudoku_matrix[row][col])
        for digit in range(1, 10):
            test_square = -1
            same_square = True
            for cell in range(9):
                if str(digit) in current_col[cell]:
                    square_row = cell // 3
                    if test_square == -1 or test_square == square_row:
                        test_square = square_row
                    else:
                        same_square = False
            if same_square:
                square_col = (col // 3) * 3
                for col_iter in range(square_col, square_col + 3):
                    if col_iter != col:
                        for row_iter in range(square_row * 3, square_row * 3 + 3):
                            temp_str = sudoku_matrix[row_iter][col_iter].replace(str(digit), '')
                            sudoku_matrix[row_iter][col_iter] = temp_str
    return sudoku_matrix


def pointing_pairs_rows(sudoku_matrix):

    for row in range(9):
        current_row = []
        for col in range(9):
            current_row.append(sudoku_matrix[row][col])
        for digit in range(1, 10):
            test_square = -1
            same_square = True
            for cell in range(9):
                if str(digit) in current_row[cell]:
                    square_col = cell // 3
                    if test_square == -1 or test_square == square_col:
                        test_square = square_col
                    else:
                        same_square = False
            if same_square:
                square_row = (row // 3) * 3
                for row_iter in range(square_row, square_row + 3):
                    if row_iter != row:
                        for col_iter in range(square_col * 3, square_col * 3 + 3):
                            temp_str = sudoku_matrix[row_iter][col_iter].replace(str(digit), '')
                            sudoku_matrix[row_iter][col_iter] = temp_str
    return sudoku_matrix


def hidden_pairs(segment):

    for digit_a in range(1, 10):
        dig_count_a = sum(str(digit_a) in s for s in segment)
        if dig_count_a == 2:
            indices_a = [indx for indx, dig_a in enumerate(segment) if str(digit_a) in dig_a]
            for digit_b in range(digit_a + 1, 10):
                dig_count_b = sum(str(digit_b) in s for s in segment)
                if dig_count_b == 2:
                    indices_b = [indx for indx, dig_b in enumerate(segment) if str(digit_b) in dig_b]
                    if indices_a == indices_b:
                        temp_str = str(digit_a) + str(digit_b)
                        segment[indices_a[0]] = temp_str
                        segment[indices_a[1]] = temp_str
    return segment


def x_wings(sudoku_matrix):
    """For each digit, scan all the rows
    if in rows "a" and "b" there is the same digit in indices a and b:
    remove the digits from indices a and b, except in rows a and b.
    """

    for digit in range(1, 10):
        for row_a in range(9):
            pos_a, pos_b = 0, 0
            for indx_a in range(9):
                if str(digit) in sudoku_matrix[row_a][indx_a]:
                    if pos_a == 0:
                        pos_a = indx_a
                    elif pos_b == 0:
                        pos_b = indx_a
                    else:
                        break
                if pos_a != 0 and pos_b != 0:
                    # Potential match
                    for row_b in range(row_a + 1, 9):
                        success = True
                        for indx_b in range(9):
                            if indx_b == pos_a or indx_b == pos_b:
                                if str(digit) not in sudoku_matrix[row_b][indx_b]:
                                    success = False
                            else:
                                if str(digit) in sudoku_matrix[row_b][indx_b]:
                                    success = False
                        if success:
                            for row in range(9):
                                if row != row_a and row != row_b:
                                    temp_str = sudoku_matrix[row][pos_a].replace(str(digit), '')
                                    sudoku_matrix[row][pos_a] = temp_str
                                    temp_str = sudoku_matrix[row][pos_b].replace(str(digit), '')
                                    sudoku_matrix[row][pos_b] = temp_str
    return sudoku_matrix


def is_solved(sudoku_matrix):
    """Checks if the sudoku is solved by examining the length of each cell string.
    e.g. len('2') returns 1, therefore that particular cell is solved.
    """

    for i in range(9):
        for j in range(9):
            if len(sudoku_matrix[i][j]) > 1:
                return False
    return True


def compute(sudoku_matrix):
    """Runs all of the checkers, including the checkers which span multiple columns/rows/squares at once."""

    count = 0
    while not is_solved(sudoku_matrix) and count < 10:
        sudoku_matrix = row_slicer(sudoku_matrix)
        sudoku_matrix = col_slicer(sudoku_matrix)
        sudoku_matrix = square_slicer(sudoku_matrix)
        sudoku_matrix = pointing_pairs_rows(sudoku_matrix)
        sudoku_matrix = pointing_pairs_cols(sudoku_matrix)
        count += 1
    sudoku_matrix = x_wings(sudoku_matrix)

    count = 0
    while not is_solved(sudoku_matrix) and count < 10:
        sudoku_matrix = row_slicer(sudoku_matrix)
        sudoku_matrix = col_slicer(sudoku_matrix)
        sudoku_matrix = square_slicer(sudoku_matrix)
        sudoku_matrix = pointing_pairs_rows(sudoku_matrix)
        sudoku_matrix = pointing_pairs_cols(sudoku_matrix)
        count += 1
    return sudoku_matrix


if __name__ == '__main__':

    print(final_sudoku_solution())
