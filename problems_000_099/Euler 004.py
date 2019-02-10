from helpers import is_palindrome


def compute(limit):
    """Finds the largest palindrome made from multiplying 2 numbers whose max sizes are limit."""

    for i in range(100, limit):
        for j in range(100, limit):
            # Cache product
            result = i * j
            if is_palindrome(result):
                yield result


if __name__ == '__main__':

    print(max(compute(1000)))
