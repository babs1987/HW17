import pool

if __name__ == "__main__":
    obj1 = pool.Pool(2)
    obj1.val = 1
    obj2 = pool.Pool()
    obj2.val = 7
    obj3 = pool.Pool()
    obj4 = pool.Pool()
    obj5 = pool.Pool()
    print(obj1.val)
    print(obj2.val)
    print(obj3.val)
    print(obj4.val)
    print(obj5.val)

