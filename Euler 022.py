def parse():
    """Returns the info from the file as a list."""

    with open('p022_names.txt') as file:
        return file.read().replace('"', "").split(',')


def score_name(name):
    """Returns the score of a single name."""

    char_offset = ord('A') - 1
    return sum(ord(char) - char_offset for char in list(name))


def score_names(names):
    """Returns the score of the list."""

    return sum(ind * score_name(name) for ind, name in enumerate(sorted(names), start=1))


if __name__ == "__main__":

    print(score_names(parse()))
