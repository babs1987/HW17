from random import randint
from time import time_ns


def lin_search(ary, el):
    for idx in range(len(ary)):  # n
        if ary[idx] == el:
            return idx

    return -1


# for size in range(1, 1000, 10):
#     ary = [randint(-1000000, 1000000) for _ in range(100 * size)]
#     el = randint(-1000000, 1000000)
#
#     start = time_ns()
#     lin_search(ary, el)
#     print(f'Size {size}: {time_ns() - start}')


# Size 101: 999900
# Size 921: 7001700
