from random import randint
from time import time_ns


# for idx in range(ary_size // 2 - 1, -1, -1):
#     heapify(ary, ary_size, idx)
def heapify(arr, size, idx):
    biggest = idx
    left = idx * 2 + 1
    right = idx * 2 + 2

    if left < size and arr[left] > arr[idx]:
        biggest = left

    if right < size and arr[right] > arr[biggest]:
        biggest = right

    if idx != biggest:
        arr[biggest], arr[idx] = arr[idx], arr[biggest]
        heapify(arr, size, biggest)


def is_heap(arr: list) -> bool:
    size = len(arr)

    for idx in range(size // 2 - 1, -1, -1):
        left = idx * 2 + 1
        right = idx * 2 + 2
        if (
            (left < size and right < size)
            and (arr[idx] < arr[left] or arr[idx] < arr[right])
        ):
            return False

    return True


ary = [randint(-100, 100) for _ in range(1000)]
# print(ary)
# ary_size = len(ary)
#
# for idx in range(ary_size // 2 - 1, -1, -1):
#     heapify(ary, ary_size, idx)
#
# print(ary, is_heap(ary))


def heap_sort(arr):
    arr_size = len(arr)
    for idx in range(arr_size // 2 - 1, -1, -1):  # n
        heapify(arr, arr_size, idx)  # log(n)

    for idx in range(arr_size - 1, 0, -1):  # n
        arr[0], arr[idx] = arr[idx], arr[0]
        heapify(arr, idx, 0)  # log(n)


# heap_sort(ary)
# print(ary)

for size in range(1, 1000, 10):
    ary = [randint(-1000000, 1000000) for _ in range(10 * size)]

    start = time_ns()
    heap_sort(ary)
    print(f'Size {size}: {time_ns() - start}')


# 99 - 162996700
# 10 - 1001200


# 10: 985800
# 99: 1000100

# Size 10: 1000400
# Size 99: 10000900



# Size 101: 3000200
# Size 981: 29003600


# Size 101: 5998600
# Size 981: 63003200


