def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class ThisIsSingletonNow:
    pass

a = ThisIsSingletonNow()
a.x=5

b = ThisIsSingletonNow()
print(b.x)