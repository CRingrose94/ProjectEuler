"""
If you want to find the last n digits of a number after doubling, you only need to keep the last n digits after each step.
Furthermore, you can improve the speed of powering by multiplying, e.g.

x ** ab = x ** a * x ** b

This can be done recursively, e.g.

x ** 16 = x ** 8 * x ** 8
        = x ** 4 * x ** 4 * x ** 4 * x ** 4
        = x ** 2 ... x ** 2

This can be more compactly calculated as:

x ** 16 = (x ** 8) ** 2
     = ((x ** 4) ** 2) ** 2
     = (((x ** 2) ** 2) ** 2) ** 2

This reduces the time by ~ its square root. n-1 opps -> sqrt(n) opps.

Python actually has a function built in (BORING!): pow(). This instead uses a fast algorithm which uses the mod too.

You can abuse the fact that the question only asks for the last 10 digits, making the answer trivial.
"""


def compute():

    return (28433 * pow(2, 7830457, 10 ** 10) + 1) % 10 ** 10


if __name__ == '__main__':

    print(compute())
