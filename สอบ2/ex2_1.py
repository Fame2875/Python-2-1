class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def __str__(self):
        out = ""
        if not self.isEmpty():
            for i in self.item:
                out += str(i) + " "
        return "Data in Stack is : "+out

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.item.pop()
        else:
            return "Can't Pop"

    def size(self):
        return len(self.item)

    def peek(self):
        if self.isEmpty():
            self.item = []
            return "[]"
        else:
            return self.item[-1]

    def bottom(self):
        if self.isEmpty():
            self.item = []
            return "[]"
        else:
            return self.item[0]

#print("output")
choice = input("Enter choice : ")
if choice == '1':
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
if choice =='2':
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
if choice =='3':  
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())  



