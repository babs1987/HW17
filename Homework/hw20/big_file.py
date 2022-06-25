import os
class FileStack:
    def __init__(self,path):
        self._path=path

    def add(self,new_string):
        with open(self._path,mode="r",encoding="utf-8") as f1,open("temp", mode="w",encoding="utf-8") as f2:
            p=""
            f2.write(new_string)
            for line in f1:
                line = line.strip()
                f2.write(p+"\n")
                p = line
            print(p)
        os.remove("stack")
        os.rename("temp","stack")


a=FileStack("stack")
a.add("NewString1")


# with open("stack",mode="w",encoding="utf-8") as f:
#     for i in range(10000):
#         f.write(f"{i} {'string lorem ipsum'}{'aaa'*5000}"+"\n")






