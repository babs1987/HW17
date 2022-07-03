from random import randint
from time import time_ns

def lin_search(ary, el):
    for idx in range(len(ary)):  # n
        if ary[idx] == el:
            return idx

    return -1