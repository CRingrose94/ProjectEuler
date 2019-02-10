def compute(limit):

    return sum(len(to_english(i)) for i in range(1, limit + 1))


def to_english(n):
    """Converts integer to string of its name with no spaces."""

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + (ones[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ones[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else "")
    else:
        raise ValueError('Number too large.')


if __name__ == '__main__':

    print(compute(1000))
