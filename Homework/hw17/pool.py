class Pool:
    _instance = []
    _current = 0

    def __new__(cls, *args, **kwargs):
        if len(Pool._instance) < 5:
            Pool._instance.append(super(Pool, cls).__new__(cls, *args, **kwargs))

            Pool._current = len(Pool._instance) - 1
            #print(f"{len(Pool._instance)} объектов")
        else:
            #print("создано уже 5")
            Pool._current = (Pool._current + 1) % 5

        return Pool._instance[Pool._current]

    def __init__(self):
        self._classes = []

for num in range(5):
    obj=Pool()
    obj.value=num

for num in range(5):
    obj = Pool()
    assert obj.value == num




