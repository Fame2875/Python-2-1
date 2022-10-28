operators = {'+', '-', '*', '/', '//', '%', '^'}
result =0
class StackCalc:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def run(self,arg):
        
        for i in range(len(self.items)):
            self.items
            if self.items[i] =='+':
               self.items.pop() 
               m1 =self.items.pop()
               m2 =self.items.pop()
               result =m1+m2
               self.items.push(result)
            elif self.items[i] =='-':
               self.items.pop() 
               m1 =self.items.pop()
               m2 =self.items.pop()
               result =m1-m2
               self.items.push(result) 
            elif self.items[i] =='*':
               self.items.pop() 
               m1 =self.items.pop()
               m2 =self.items.pop()
               result =m1*m2
               self.items.push(result)  
            elif self.items[i] =='/':
               self.items.pop() 
               m1 =self.items.pop()
               m2 =self.items.pop()
               result =m1/m2
               self.items.push(result)  
            elif self.items[i] =='DUP':
               self.items.pop()
               m1 =self.items.pop() 
               result = m1*2
               self.items.push(result) 
            elif self.items[i] =='POP':
               self.items.pop() 
               self.items.pop() 
            #elif self.items[i] =='PSH':
               ## m2=self.items.pop()
               # result =m1+m2                   
        print(self.items.pop())    


       






print("* Stack Calculator *")
arg = input("Enter arguments : ").split(" ")
print(arg)
machine = StackCalc()
machine.run(arg)
#print(machine.getValue())