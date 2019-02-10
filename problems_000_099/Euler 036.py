from helpers import is_palindrome


def compute(limit):

    for i in range(limit):
        if is_palindrome(i) and is_palindrome(bin(i)[2:]):
            yield i


if __name__ == '__main__':

    print(sum(compute(1000000)))
