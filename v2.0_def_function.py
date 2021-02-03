import random
list1 = []


def Xunhuan(zz, aa, jiafa=False, jianfa=False):
    count = 0
    while count <= zz:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        # a+b

        if jiafa == True:
            c = a + b
            if c <= aa:
                count += 1
                add = "{}+{}=__".format(a, b)
                list1.append(add)
            else:
                continue
        elif jianfa == True:
            c = a - b
            if c > 0:
                count += 1
                div = "{}-{}=__".format(a, b)
                list1.append(div)

    print(list1)


Xunhuan(10, 10, jianfa=True)
