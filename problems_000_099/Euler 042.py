from string import ascii_uppercase


def parse_file():
    """Return the document as a list."""

    with open('../euler_files/p042_triwords.txt') as euler_file:
        return euler_file.read().replace('"', "").split(',')


def assign_number():
    """Creates a dictionary where every letter has a numerical value"""

    return {letter: count for count, letter in enumerate(ascii_uppercase, start=1)}


def triangle_gen(limit):

    return [n * (n + 1) / 2 for n in range(limit)]


def compute(limit):

    compare = triangle_gen(limit)
    count = 0

    for word in parse_file():
        if sum(assign_number()[char] for char in word) in compare:
            count += 1

    return count


if __name__ == '__main__':

    print(compute(50))
