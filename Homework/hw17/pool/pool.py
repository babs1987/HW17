class Pool:
    _instance = []
    _current = 0
    _count=5

    def __new__(cls,message=None, *args, **kwargs):
        if message is None:
            message=cls._count
        if len(Pool._instance) < message:
            cls._instance.append(super().__new__(cls,*args, **kwargs))
            cls._count=message
            cls._current = len(cls._instance) - 1
        else:
            #print("создано уже 5")
            cls._current = (cls._current + 1) % message

        return cls._instance[cls._current]

