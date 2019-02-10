def fib(limit):

    zero, first, count = 0, 1, 1

    while len(str(first)) < limit:
        next = first + zero

        zero, first = first, next
        count += 1
        
    return count


if __name__ == '__main__':
    print(fib(1000))
