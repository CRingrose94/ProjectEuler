def compute():

    i = 286
    j = 166
    k = 144

    while True:
        tri = i * (i + 1) // 2
        pen = j * (j * 3 - 1) // 2
        hex = k * (k * 2 - 1)
        minim = min(tri, pen, hex)
        if minim == max(tri, pen, hex):
            return tri
        if minim == tri:
            i += 1
        if minim == pen:
            j += 1
        if minim == hex:
            k += 1


if __name__ == '__main__':

    print(compute())
