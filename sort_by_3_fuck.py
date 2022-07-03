print(bin(25),bin(21))

def sort_by_binary_ones (numList):
    return sorted(numList,key=lambda a:(-bin(a)[2:].count("1"),len(bin(a)[2:]),a))

print(sort_by_binary_ones([1, 5, 21, 7, 44, 99, 50, 51, 49, 80, 33, 25]))