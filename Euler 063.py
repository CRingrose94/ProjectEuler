"""
i^j is always at least j + 1 digits when i > 10.
even when i is small (2), i^j is too large for j > 22.
Hence, i is in range 1, 10 and j is in range 1 and 22.
"""


def compute():

    powerful_digit_sum = 0

    for i in range(1, 10):
        for j in range(1, 22):
            if len(str(i ** j)) == j:
                powerful_digit_sum += 1
    return powerful_digit_sum


if __name__ == '__main__':

    print(compute())
