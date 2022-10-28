class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items == list

    def enQueue(self, i):
        self.items.append(i)  # ใส่ i ท้ายแถว

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
           return ", ".join(self.items)


Input = input("Enter Input : ").split(",")
q = Queue()
out_list =[]
for i in range(len(Input)):
    m = (Input[i]).split(" ")
    if len(m) > 1:
        if m[0] =='E' :
            q.enQueue(m[1])
            print(q.peek())
    if len(m) == 1:
        if m[0] == 'D':
            if q.size() > 0:
             out = q.deQueue()
             out_list.append(out)
             print(f"{out} <-", end=" ")
             print(q.peek())
            elif q.size() == 0:
                print(q.peek())
if len(out_list ) > 0:                
  print(", ".join(out_list),end=" : ")
  print(q.peek())
if  len(out_list ) == 0:
    print("Empty",end=" : ")
    print(q.peek())

