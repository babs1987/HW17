from random import randint, choice

def bubble_sort(a: list) -> None:  # O(n*n)
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue

            if i < j:
                if a[i] > a[j]:  # swap
                    a[i], a[j] = a[j], a[i]

            if i > j:
                pass