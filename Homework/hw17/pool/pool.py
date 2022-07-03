from typing import Optional
from random import choice


class Pool2:
    _instance = []
    _current = 0
    _count = 5

    def __new__(cls, message=None, *args, **kwargs):
        if message is None:
            message = cls._count
        if len(cls._instance) < message:
            cls._instance.append(super().__new__(cls, *args, **kwargs))
            cls._count = message
            cls._current = len(cls._instance) - 1
        else:
            cls._current = (cls._current + 1) % message

        return cls._instance[cls._current]


# teacher
# паттерн пул

class Pool:
    _objects = []
    _size = None
    _objects_index = 0

    def __new__(cls, *args, size: Optional[int] = None, **kwargs):
        if size is None and cls._size is None:
            raise RuntimeError(f"You should define Pool size before using it")
        elif size is None:
            size = cls._size
        elif cls._size is None:
            cls._size = size
        assert size>0,"Size must to be positive integer"
        if len(cls._objects) < size:
            new_obj = super().__new__(cls, *args, **kwargs)
            cls._objects.append(new_obj)

        result = cls._objects[cls._objects_index]
        cls._objects_index = (cls._objects_index + 1) % size
        return result
