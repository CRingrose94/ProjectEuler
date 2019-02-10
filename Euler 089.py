def shorten_numerals(roman_string):
    """A dict might be more logical but this works and is fast."""

    replacements = [('VIIII', 'IX'),
                    ('IIII', 'IV'),
                    ('LXXXX', 'XC'),
                    ('XXXX', 'XL'),
                    ('DCCCC', 'CM'),
                    ('CCCC', 'CD')]

    for original, shortened in replacements:
        roman_string = roman_string.replace(original, shortened)
    return roman_string


def compute():

    # counts
    original, shortened = 0, 0

    with open("p089_roman.txt") as file:
        for line in file:
            original += len(line)
            shortened += len(shorten_numerals(line))

    return original - shortened


if __name__ == '__main__':

    print(compute())
