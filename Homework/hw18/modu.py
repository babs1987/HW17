
from inspect import getmembers, isfunction
from search.linear_search import *

import sort.bubble as bublic

if __name__ == '__main__':
    a = [2, 5, 3, 4, 7, 8]
    bublic.bubble_sort(a)
    print(lin_search(a, 3))
    print(a)

    functions_of_module = lambda func: [x[0] for x in getmembers(func) if isfunction(x[1])]

    print(functions_of_module(bublic))