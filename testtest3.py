class human():
    count = 0

    def __init__(self):
        pass

    def add(self, haha=False, bb=None):
        if haha == False:
            print("false")
            self.ha = bb
            human.count += 1
            print(human.count)
        else:
            print("true")


h = human()
h.add(bb=4)
print(h.ha)
