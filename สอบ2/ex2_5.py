class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items == list

    def enQueue(self, i):
        self.items.append(i)

    def enQueuefix(self, pos, a):
        self.items.insert(pos, a)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return "\n".join(self.items)

    def peeklast(self):
        return self.items[-1]
    def listq(self):
        return self.items    
Input = input("Enter Input : ").split("/")
book = Input[0].split(" ")
ins = Input[1].split(",")
f =True
q = Queue()
for i in range(len(book)):
    q.enQueue(book[i])
for i in range(len(ins)):
    m = ins[i].split(" ")
    if m[0] == 'D':
        if q.size() > 0:
            q.deQueue()
    if m[0] == 'E':
        q.enQueue(m[1]) 
check =[]
for i in q.listq() :
    if i not in check:
        check.append(i)
    elif i in check:
        f = False
if f == True:
    print("NO Duplicate") 
if f == False:           
    print("Duplicate")