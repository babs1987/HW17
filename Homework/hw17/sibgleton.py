def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class Hello:
    pass

hello1 = Hello()
hello1.name = 'Gosha'

hello2 = Hello()
assert hello2.name == 'Gosha'