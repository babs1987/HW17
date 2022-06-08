import os
import pickle


class Car:
    def __init__(self, model: str, year: int, power: float):
        self._model = model
        self._year = year
        self._power = power

    def __str__(self):
        return f"{self._model},{self._year},{self._power}"

    def save_to_file(self, path):
        directory = path[:path.rindex("\\")]
        if not os.path.exists(directory):
            os.mkdir(directory)
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except IOError:
            return "FileNotFound"






bmw = Car("БМВ", 1984, 130.5)

bmw.save_to_file("C:\Cars\\bmw.txt")

print(bmw.read_from_file("C:\Cars\\bmw.txt"))
"""
забавно что заглавные символы не экранируются
"""