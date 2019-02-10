def collatz(n):
    """Returns the number of terms in a collatz sequence for a starting number, n.
    A collatz sequence is defined as:    n -> n / 2 if n is even,
                                         n -> 3n + 1 if n is odd.
    """
    count = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
    return count


def largest(limit):
    """Returns the number below <limit> which breeds the longest collatz sequence."""

    current_largest = 0

    for i in range(1, limit):
        if collatz(i) > current_largest:
            current_largest = collatz(i)
            ans = i
    return ans


if __name__ == '__main__':

    print(largest(10 ** 6))
