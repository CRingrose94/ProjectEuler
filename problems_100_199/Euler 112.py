def compute(limit):

    asc_desc = 525
    bouncy = 475
    i = 1001

    while bouncy / (asc_desc + bouncy) != limit:

        if ''.join(sorted(str(i))) == str(i) or ''.join(sorted(str(i), reverse=True)) == str(i):
            asc_desc += 1
        else:
            bouncy += 1
        i += 1

    return i - 1


if __name__ == '__main__':

    print(compute(0.99))
