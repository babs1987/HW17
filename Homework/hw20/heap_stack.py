ary = [("element1", 17), ("element3", 66), ("element4", 43), ("element5", 5),('chechnya', 95)]


class PrioQueue:
    def __init__(self, array):
        self._array = array
        self.len = len(array)
        self.to_heap()
    def __len__(self):
        self.len = len(self._array)

    def heapify(self, arr, size, idx):
        biggest = idx
        left = idx * 2 + 1
        right = idx * 2 + 2

        if left < size and arr[left][1] > arr[idx][1]:
            biggest = left

        if right < size and arr[right][1] > arr[biggest][1]:
            biggest = right

        if idx != biggest:
            arr[biggest], arr[idx] = arr[idx], arr[biggest]
            self.heapify(arr, size, biggest)

    def to_heap(self):
        for idx in range(self.len // 2 - 1, -1, -1):
            self.heapify(self._array, self.len, idx)

    def add(self, element: tuple[str, int]):
        self._array.append(element)
        self.len+=1
        self.to_heap()

    def pop(self):
        self._array.pop(0)
        self.len -= 1
        self.to_heap()





a = PrioQueue(ary)

a.add(("piroman",77))

a.pop()
a.pop()
print(a._array)
