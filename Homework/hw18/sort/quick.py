from random import randint, choice
from time import time_ns


def quick_sort(a: list) -> list:  # log(n) * n | n * n
    if len(a) <= 1:
        return a

    # [....*.....]
    el = choice(a)

    # [...][***][....]
    equal_el = [el] * a.count(el)
    left = quick_sort([x for x in a if x < el])  # n / 2  --  0
    right = quick_sort([x for x in a if x > el])  # n / 2  -- n

    return left + equal_el + right


# ary = [randint(-100, 100) for _ in range(10)]
# print(ary)
# print(quick_sort(ary))


for size in range(1, 1000, 10):
    ary = [randint(-1000000, 1000000) for _ in range(10 * size)]

    start = time_ns()
    quick_sort(ary)
    print(f'Size {size}: {time_ns() - start}')

# 99 - 162996700
# 10 - 1001200


# 10: 985800
# 99: 1000100
