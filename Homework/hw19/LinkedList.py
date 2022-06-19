import copy
from typing import Optional

class Node:
    def __init__(self, value: int, next_prt: Optional['Node'] = None):
        self.value = value
        self.next_prt = next_prt


class LinkedList:
    def __init__(self, *args):
        self.len = len(args)
        if len(args) == 1:
            self.head = args[0]
        elif len(args)>1:
            self.head = Node(args[0])
            temp = self.head
            for i in range(1, len(args)):
                temp.next_prt = Node(args[i])
                temp = temp.next_prt

    def __len__(self):
        return self.len

    def append(self, value):
        if self.len == 0:
            self.len = 1
            self.head = Node(value)

        else:
            self[self.len - 1].next_prt = Node(value)
            self.len += 1

    def print_all(self):
        for i in range(len(self)):
            print(self[i].value, end=" ")
        print()

    def __getitem__(self, index):
        i = 0
        temp = self.head
        while i < index and temp.next_prt:
            temp = temp.next_prt
            i += 1
        if i == index:
            return temp
        else:
            raise KeyError

    def __add__(self, other):
        a = copy.copy(self)

        a[a.len - 1].next_prt = other.head
        a.len = a.len + other.len
        return a

    def prepend(self,value):
        t = self.head
        print(t.value)
        self.head = Node(value)
        self.head.next_prt = t
        self.len += 1

    def insert(self, value, index):
        if index > self.len:
            raise KeyError
        temp = self[index]
        if index!=0 :
            self[index - 1].next_prt = Node(value)
            self.len += 1
            self[index].next_prt = temp

        else:
            self.prepend(value)


li = LinkedList(1, 2, 3, 4, 5)
li.prepend(0)
li2=LinkedList()
print(li2.len,"длина li2")
li2.append(6)

li3=LinkedList(Node(666))
li3.insert(665,0)

li4=li3+li2



print(f"li:0+1,2,3,4,5 len :{len(li)}")
li.print_all()

print(f"li2: None+6 len : {len(li2)}")
li2.print_all()

print(f"li3: 665+Node(666) len : {len(li3)}")
li3.print_all()

print("li3+li2")
li4.print_all()

# li = LinkedList()
# li.append(6)
# li.append(7)
# li.append(8)
# li.append(9)
# li2=LinkedList(Node(5))
# li2.append(6)
#
# li.print_all()
# li.insert(66, 3)
# li.print_all()
#
# li3=li+li2
#
# li.print_all()
# li3.print_all()

# print(li[3].value)
