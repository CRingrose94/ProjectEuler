"""
Draw one horizontal line at base, and another one unit above it.
Draw a vertical line at the far left.
Draw another vertical line right of the left vertical line.
Move the second vertical line right one unit until it hits the right edge. Count each step.
Move the first vertical line across one unit.
Repeat movements of second vertical line.
Move second horizontal line repeat etc.

This entire process can actually be done analytically.

Number of rectangles in a rectangle is given by:
    (w ** 2 + w) * (h ** 2 + h) / 4

If w, h = 100, 100 there are 2.5 * 10 ** 7 rectangles, so this serves as a good approximate limit.
"""


def compute(limit_h, limit_w):

    target = 2 * 10 ** 6
    current_closest = 1000

    for h in range(10, limit_h):
        for w in range(10, limit_w):
            proximity = abs(target - (w ** 2 + w) * (h ** 2 + h) / 4)
            if proximity < current_closest:
                current_closest = proximity
                area = w * h
    return area


if __name__ == '__main__':

    print(compute(100, 100))
