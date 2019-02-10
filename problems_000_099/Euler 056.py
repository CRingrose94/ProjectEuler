def compute():

    current_max = 0

    for i in range(100):
        for j in range(100):

            total = sum(int(digit) for digit in str(i ** j))

            if total > current_max:
                current_max = total

    return current_max


if __name__ == '__main__':

    print(compute())
