from random import randint, choice



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
