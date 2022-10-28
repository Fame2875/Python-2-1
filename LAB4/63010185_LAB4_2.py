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


class EsQueue:
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


Input = input("Enter Input : ").split(",")
q = Queue()
preq = EsQueue()
out_list = []
emp = False
for i in range(len(Input)):
    m = (Input[i]).split(" ")
    if len(m) > 1:
        if m[0] == 'EN':
            q.enQueue(m[1])
            emp = True

        if m[0] == 'ES':
            preq.enQueue(m[1])
            emp = True         
    if len(m) == 1:
        if m[0] == 'D':
            if preq.size() > 0:
                
                out = preq.deQueue()
                out_list.append(out)
                print(out_list.pop())
            elif preq.size() == 0:
                if q.size() > 0:
                    out = q.deQueue()
                    out_list.append(out)
                    print(out_list.pop())
                      
               # if q.size() == 0 and emp == True:
                 #   print("\n".join(out_list))
                  #  out_list.clear()
                  #  emp = False 
                elif q.size() == 0 :
                    print("Empty")
                    