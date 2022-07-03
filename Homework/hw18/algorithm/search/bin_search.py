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



