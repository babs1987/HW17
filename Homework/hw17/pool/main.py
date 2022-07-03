import pool

if __name__ == "__main__":
    obj1 = pool.Pool(size=2)
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
    print("____________________________________________")
    obj9 = pool.Pool2(2)
    obj9.val = 1
    obj10 = pool.Pool2()
    obj10.val = 7
    obj12 = pool.Pool2()
    obj13 = pool.Pool2()
    obj14 = pool.Pool2()
    print(obj9.val)
    print(obj10.val)
    print(obj12.val)
    print(obj13.val)
    print(obj14.val)
