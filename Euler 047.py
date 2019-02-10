def compute(limit, n_f, n_s):

    count = 0
    limit += n_s
    factors = [0] * limit

    ans = []

    for n in range(2, limit):
        if factors[n] == n_f:
            count += 1
            if count == n_s:
                ans.append(n - n_s + 1)
                count -= 1
        else:
            count = 0
            if factors[n] == 0:
                factors[n::n] = [x + 1 for x in factors[n::n]]

    return min(ans)


if __name__ == '__main__':

    print(compute(300000, 4, 4))
