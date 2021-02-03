import random
list1 = []
book = open('D:\\zzz3.txt', 'w')

count = 0
number = 0
while count <= 90:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = a+b
    if c <= 10:
        count += 1
        add = "{}+{}=__".format(a, b)

        list1.append(add)
    else:
        continue
while number <= 90:
    e = random.randint(0, 10)
    f = random.randint(0, 10)
    c = e-f
    if c > 0:
        number += 1
        div = "{}-{}=__".format(e, f)

        list1.append(div)
    else:
        continue
print(list1)
random.shuffle(list1)

print(list1)
for x in list1:
    book.write(x)
book.close()
