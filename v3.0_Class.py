import random
from abc import ABC, ABCMeta


class xunhuan():
    count = 0
    list1 = []

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ADD(self, limit=False, aa=None, bb=None):
        if limit == False:
            c = self.a+self.b
            print(c)
        elif limit == True:
            while xunhuan.count <= aa:
                self.a = random.randint(0, 10)
                self.b = random.randint(0, 10)
                c = self.a + self.b
                if c <= bb:
                    xunhuan.count += 1
                    add = "{}+{}=__".format(self.a, self.b)
                    xunhuan.list1.append(add)
                    print(xunhuan.list1)
                else:
                    continue


z1 = xunhuan(3, 4)
z1.ADD()
