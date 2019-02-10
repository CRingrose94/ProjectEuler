from itertools import combinations


def values(k):
    """Recursively returns all operation combinations for the concatenated digits, k"""

    if len(k) == 2:
        a, b = k[0], k[1]
        return list({a + b, a - b, b - a, a * b, b and a / b, a and b / a})
    result = []
    for pos, num in enumerate(k):
        for j in values(k[:pos] + k[pos + 1:]):
            result += values([j, num])
    return list(set(result))


def compute():

    maximum = []

    for digits in combinations('0123456789', 4):
        x, k = 1, [int(digit) for digit in digits]
        u = values(k)
        while x in u:
            x += 1
        maximum.append((k, x))

    return ''.join(([str(n) for n in max(maximum, key=lambda u: u[1])[0]]))


if __name__ == '__main__':

    print(compute())


'''
Could use a reverse Polish calc instead. 
'''