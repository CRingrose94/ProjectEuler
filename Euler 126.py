def cubes_per_layer(x, y, z, n):
    """Dimensions x, y, z and layer n"""

    return 2 * (x * y + x * z + y * z) + 4 * (x + y + z + n - 2) * (n - 1)


def compute(limit):
    """Create a list of length <limit>, where each entry is empty.
    For all cuboid shapes, calculate number of cubes in layers (up to x layers)
    Increment list value for appropriate list index
    Return index for which the value is 1000
    """

    # Here's the null list
    layers_list = (limit + 1) * [0]

    # Lots of complicated range shortening follows. This is basically just for speed-up.
    for x in range(1, limit + 1):
        for y in range(x, limit // x + 2):
            if x * y > limit:
                break
            for z in range(y, limit // max(x, y) + 2):
                if x * z > limit or y * z > limit:
                    break
                for n in range(1, limit):
                    layers = cubes_per_layer(x, y, z, n)
                    if layers > limit:
                        break
                    layers_list[layers] += 1

    for index in range(len(layers_list)):
        if layers_list[index] == 1000:
            return index


if __name__ == '__main__':

    print(compute(20000))
