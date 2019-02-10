def compute(limit):

    ans = [0 for i in range(limit + 1)]

    for i in range(1, 500):
        for j in range(i, 501 - i):
            k = (i * i + j * j) ** 0.5

            if k - int(k) == 0:
                ans[int(i + j + k)] += 1

    return ans.index(max(ans))


if __name__ == '__main__':

    print(compute(1000))
