def compute(limit):
    """Calculates the first triangle number to have limit divisors."""

    tri_num, next_num, divisors = 0, 0, 0

    while divisors <= limit:

        # Increment to next triangle number.
        next_num += 1
        tri_num += next_num

        sq_root = tri_num ** 0.5
        divisors = 2 * sum(tri_num % n == 0 for n in range(1, int(sq_root)))

        if sq_root == int(sq_root):
            divisors += 1

    return tri_num


if __name__ == '__main__':

    print(compute(500))
