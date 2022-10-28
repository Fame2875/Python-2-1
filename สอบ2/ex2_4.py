class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.size = 0

    def __str__(self):
        c = self.head.next
        string = ""
        while c is not None:
            string += str(c.data) 
            if c.next != None:
                string+=" <- "
            c = c.next
        return string

    def append(self, data):
        current = self.head
        while current.next is not None: #ไล่จากตัวแรกของlinklistไปยังตัวสุดท้าย ถ้าเจอตัวสุดท้ายถึงออกจากลูป
            current = current.next
        current.next = Node(data, None)
        self.size += 1
    
    def getHead(self):
        return self.head.next
    def getTail(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        return cur
    

l1 = SinglyLinkedList()
a=0
print(" *** Re order ***")
inp = input('Enter Input : ').split()
for i in inp:
    l1.append(i)
print("Before :",l1)
cur = l1.getHead()
while cur.next is not None :
    if cur.next.data == '0':
        l1.getTail().next = l1.head.next
        l1.head.next = cur.next
        cur.next = None
        break
    cur = cur.next
print("After :",l1)