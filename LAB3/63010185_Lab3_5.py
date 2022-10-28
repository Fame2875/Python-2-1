class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "$"

    def peek(self):
        if self.isEmpty() == True:
            self.items = []
            return "[]"
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def clearStack(self):
        for i in range(self.size()):  # G+A+(U-R)^I
            self.pop()
        return self.items

def parking(maxspace, totalcar, order, RecentcarNum):
    s=Stack()
    
    totalcar = [int(x) for x in totalcar.split(',')]
    maxspace_int = int(maxspace)
    RecentcarNum_int = int(RecentcarNum)
    #print(totalcar)

    for i in totalcar:

        s.push(i)
        #print(s.size())
        #print(totalcar)
    if 0 in s.items:
        #print("WORK")
        s.pop()
    if order[0] == 'a':
        
        if RecentcarNum_int in s.items:
            return f'car {RecentcarNum} already in soi',s.items
        elif s.size() == maxspace_int:
            return f'car {RecentcarNum} cannot arrive : Soi Full',s.items
        else : 
            s.push(int(RecentcarNum))
            return f'car {RecentcarNum} arrive! : Add Car {RecentcarNum}',s.items
    else:
        if s.isEmpty():
            return f'car {RecentcarNum} cannot depart : Soi Empty',s.items
        if RecentcarNum_int not in s.items:
            return f'car {RecentcarNum} cannot depart : Dont Have Car {RecentcarNum}',s.items
        else:
            while RecentcarNum_int in s.items:
                s.items.reverse()
                s.pop()
                s.items.reverse()

            return f'car {RecentcarNum} depart ! : Car {RecentcarNum} was remove',s.items

    return 0

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
#total = s.split(',')
parking(m, s, o, n)
print(parking(m, s, o, n)[0])
print(parking(m, s, o, n)[1])
m,n = int(m),int(n)