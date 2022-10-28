from decimal import Decimal as D


class Stack():

    def __init__(self, *ls):
        self.items = [x for x in ls]

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class StackCalc:

    def __init__(self):
        self.stack = Stack()

    def run(self, arg):
        s = arg.split()
        for i in s:
            if i not in "+-*/" and i not in ["DUP", "POP", "PSH"]:
                self.stack.push(i)
            elif i in "+-*/":
                try:
                    x = D(self.stack.pop())
                    y = D(self.stack.pop())
                    if i == "+":
                        self.stack.push(x+y)
                    elif i == "-":
                        self.stack.push(x-y)
                    elif i == "*":
                        self.stack.push(x*y)
                    elif i == "/":
                        self.stack.push(x/y)
                except:
                    print("Invalid instruction: " + arg[0])
                    
            else:
                if i == "DUP":
                    self.stack.push(self.stack.peek())
                elif i == "POP":
                    self.stack.pop()

    def getValue(self):
        if self.stack.size() > 0:
            return self.stack.pop()
        else:
            return 0


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
