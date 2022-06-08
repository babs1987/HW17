import os

class PathDoesNotExists(FileNotFoundError):
    pass

class Path:
    path = ""

    def __init__(self, path):
        self.path = path

    @classmethod
    def create_dir(cls, dir: str):
        try:
            os.mkdir(cls.path + dir)
            return Path(dir)
        except FileExistsError:
            print("Path already exists")
            return Path(dir)

    def __add__(self, other: str):
        return self.path + "\\" + other

    def __truediv__(self, other: str):
        if os.path.isdir(self.path + other + "\\"):
            return Path(self.path + other + "\\")
        else:
            raise PathDoesNotExists

    def __str__(self):
        return self.path

    def __repr__(self):
        return self.__str__()
pathy = Path("C:\\")

try:
    new_path = pathy / "AMD"
except PathDoesNotExists:
    print("Не, братан, нет такого каталога")
else:
    print("Каталог есть")

c_mon=pathy.create_dir("C:\\AMD\\c_monyyy")
print(c_mon)

assert os.path.exists(str(c_mon))