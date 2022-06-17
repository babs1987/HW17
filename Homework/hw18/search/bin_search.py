from random import randint
from time import time_ns


def bin_search(ary, el):
    size = len(ary)
    center = size // 2

    if size == 0:
        return -1

    if ary[center] == el:
        return center

    if size == 1:
        return -1

    if ary[center] < el:
        return bin_search(ary[center + 1:], el)
    else:
        return bin_search(ary[:center], el)


# for size in range(1, 1000, 10):
#     ary = [randint(-1000000, 1000000) for _ in range(100 * size)]
#     ary.sort()
#     el = randint(-1000000, 1000000)
#
#     start = time_ns()
#     bin_search(ary, el)
#     print(f'Size {size}: {time_ns() - start}')


# Size 101: 999900
# Size 921: 7001700

# Size 201: 998100
# Size 921: 2001600
