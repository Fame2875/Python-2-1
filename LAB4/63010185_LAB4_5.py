class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

class Stack():

    def __init__(self, *ls):
        self.items = [x for x in ls]

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


f = input("Enter Input (Normal, Mirror) : ").split()

mirror = "".join(reversed(f[1]))
normal = "".join(f[0])

mirs = Stack()
nors = Stack()
mirq = Queue()
mire = 0
nore = 0
failed = 0
for i in mirror:
    mirs.push(i)
    index = mirs.size()-1
    if mirs.size() >=3 and mirs.items[index] == mirs.items[index-1] and mirs.items[index] == mirs.items[index-2]:
        for x in range(3):
            mirs.pop()
        mirq.enqueue(i)
        mire = mire + 1

trap = False if mirq.size() == 0 else True

if trap == False:
    for i in normal:
        nors.push(i)
        index = nors.size()-1
        if nors.size()>=3 and nors.items[index] == nors.items[index-1] and nors.items[index] == nors.items[index-2]:
            for x in range(3):
                nors.pop()
            nore = nore + 1
    print("NORMAL :")
    print(nors.size())
    if nors.size() == 0:
        print("Empty")
    else:
        print("".join(reversed(nors.items)))
    print("{} Explosive(s) ! ! ! (NORMAL)".format(nore))
else:
    for i in normal:
        nors.push(i)
        index = nors.size()-1
        if nors.size() >= 3 and nors.items[index] == nors.items[index-1] and nors.items[index] == nors.items[index-2] and mirq.size() != 0:
            temp = nors.pop()
            nors.push(mirq.dequeue())
            nors.push(temp)
            index = nors.size() - 1
            if nors.size() >= 3 and nors.items[index] == nors.items[index - 1] and nors.items[index] == nors.items[index - 2]:
                for x in range(3):
                    nors.pop()
                failed = failed + 1
        elif nors.size() >= 3 and nors.items[index] == nors.items[index-1] and nors.items[index] == nors.items[index-2] and mirq.size() == 0:
            for x in range(3):
                nors.pop()
            nore = nore + 1
    print("NORMAL :")
    print(nors.size())
    if nors.size() == 0:
        print("Empty")
    else:
        print("".join(reversed(nors.items)))
    print("{} Explosive(s) ! ! ! (NORMAL)".format(nore))
    if failed != 0:
        print("Failed Interrupted {} Bomb(s)".format(failed))

print("------------MIRROR------------")
print(": RORRIM")
if mirs.size() == 0:
    print("0")
    print("ytpmE")
else:
    print(mirs.size())
    print("".join(reversed(mirs.items)))
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(mire))