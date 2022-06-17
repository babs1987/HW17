from random import randint
from time import time_ns


def bubble_sort(a: list) -> None:   # O(n*n)
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue

            # [...i...j....]
            if i < j:
                if a[i] > a[j]:  # swap
                    a[i], a[j] = a[j], a[i]
                    # tmp = a[i]
                    # a[i] = a[j]
                    # a[j] = tmp
            if i > j:
                pass


# for size in range(1, 100):
#     ary = [randint(-100, 100) for _ in range(10 * size)]
#
#     start = time_ns()
#     bubble_sort(ary)
#     print(f'Size {size}: {time_ns() - start}')

# 99 - 162996700
# 10 - 1001200
