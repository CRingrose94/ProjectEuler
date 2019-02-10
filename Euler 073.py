"""
A Stern Brocot tree is a binary tree whose outermost branches give the fractions between 0 and 1.
Importantly, the fractions are properly reduced.

Taking the sequence of these fractions between two values gives a Farey sequence.

This links into all sorts of weird stuff like Ford circles.

"""


from math import gcd
###################
# ONE LINE WONDER #
###################
print(sum(1 for d in range(2, 12001) for n in range(1, d) if (n*3 > d) and (n*2 < d) and gcd(n, d) == 1))


def stern_brocot(n):

    states = [(0, 1, 1, 1)]
    result = []
    while len(states) != 0:
        a, b, c, d = states.pop()
        if a + b + c + d <= n:
            result.append((a + c, b + d))
            states.append((a, b, a + c, b + d))
            states.append((a + c, b + d, c, d))

    return result


def compute(limit):

    count = 0
    tree = stern_brocot(limit)
    for pair in tree:
        if 1 / 3 < pair[0] / pair[1] < 1 / 2:
            count += 1

    return count
