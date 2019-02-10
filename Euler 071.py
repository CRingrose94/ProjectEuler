"""
Generate two lists, n and d, each with range 1 to 1000000.
For all pairs where HCF(n, d) == 1 and n < d, find n/d.
Find the value of n/d which is closest, but no greater than 3/7.

Create a dictionary with n as the key, and n/d as the value.

ALTERNATIVELY

Start with 3/7 and count down until you reach the next fraction.
I think this is the trick to making it the minimum number of iterations.
"""


def compute(limit):

    n_max, d_max = 0, 1

    for d in range(2, limit + 1):
        n = d * 3 // 7
        if d % 7 == 0:
            n -= 1
        if n * d_max > d * n_max:
            n_max = n
            d_max = d
    return n_max


if __name__ == '__main__':

    print(compute(10 ** 6))


"""
Having seen the answer, 3/7 == 428,571/999,999. 
Grooooooan.
Should have checked the largest multiple of 7 below a million.
"""
