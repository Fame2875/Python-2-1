class Queue:

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items == list

    def enQueue(self, i):
        self.items.append(i)  # ใส่ i ท้ายแถว

    def enQueuefix(self, pos, a):
        self.items.insert(pos, a)

    def deQueue(self):
        return self.items.pop(0)  # เอาตัวหน้าออก

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
havebook = Input[0].split(" ")
insertbook = Input[1].split(",")
dup_on =True
q = Queue()
for i in range(len(havebook)):
    q.enQueue(havebook[i])
for i in range(len(insertbook)):
    m = insertbook[i].split(" ")
    if m[0] == 'D':
        if q.size() > 0:
            q.deQueue()
    if m[0] == 'E':
        q.enQueue(m[1]) 
ducheck =[]
for i in q.listq() :
    if i not in ducheck:
        ducheck.append(i)
    elif i in ducheck:
        print("Duplicate")
        dup_on = False
if dup_on == True:
    print("NO Duplicate")        

