from helpers import is_palindrome


def reverse_and_add(number):

    return number + int(str(number)[::-1])


def lychrel(number):

    count = 0
    a = reverse_and_add(number)
    if is_palindrome(a):
        return False
    while count < 50 and not is_palindrome(a):
        a = reverse_and_add(a)
        if is_palindrome(a):
            return False
        count += 1
    return True


def compute(limit):

    count = 0
    for j in range(50, limit):
        if lychrel(j):
            count += 1
    return count


if __name__ == '__main__':

    print(compute(10000))
