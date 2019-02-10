from itertools import count


def compute():

    num_digits = 0
    data = {}

    for i in count():
        digits = [int(char) for char in str(i ** 3)]
        digits.sort()
        num_class = ''.join(str(digit) for digit in digits)

        if len(num_class) > num_digits:
            cands = [lowest for (lowest, counter) in data.values() if counter == 5]
            if len(cands) > 0:
                return str(min(cands) ** 3)
            data = {}
            num_digits = len(num_class)

        lowest, counter = data.get(num_class, (i, 0))
        data[num_class] = (lowest, counter + 1)


if __name__ == '__main__':

    print(compute())
