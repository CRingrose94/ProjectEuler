from itertools import permutations


def read_file():
    """Reads file, keeping only words of five or more letters.
    Bit of a clusterfuck simply due to the original file's formatting.
    """
    return [word.strip('"') for word in open('../euler_files/p098_words.txt', 'r').readline().split(',') if len(word) >= 5]


def is_square(integer):

    return round(integer ** 0.5) ** 2 == integer


def test_square_anagram(string_a, string_b):
    """Could be rewritten as a generator but it's very fast already."""

    max_square = 0
    letters = ''.join(set(string_a))

    for l in permutations(list('0123456789'), len(letters)):

        # Define string translations.
        dic = string_a.maketrans(letters, ''.join(l))

        # Apply string translations and convert back to integers.
        n = int(string_a.translate(dic))
        m = int(string_b.translate(dic))

        # Test if the strings are both anagrams and squares.
        if m != n and len(str(n)) == len(str(m)) == len(string_a) and is_square(n) and is_square(m):
            max_square = max(n, m, max_square)

    return max_square


def compute():

    words = read_file()
    wsort = [sorted(word) for word in words]

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if wsort[i] == wsort[j]:
                square = test_square_anagram(words[i], words[j])
                if square > 0:
                    # If you would like all square anagram pairs, simply print rather than return.
                    return words[i], words[j], square


if __name__ == '__main__':

    print(compute())
