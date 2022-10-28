precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}


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


Input = input('Enter Infix : ')
S = Stack()
ans = ""

# print('Postfix : ', end='')

### Enter Your Code Here ###
for cha in Input:

    if (cha >= 'A' and cha <= 'Z') or (cha >= 'a' and cha <= 'z'):
        ans += cha
    elif cha == '(':
        S.push(cha)
    elif cha == ')':
        while S.peek() != '(':
            ans += S.items[-1]
            S.pop()
        S.pop()  # pop the last '('
    else:
        while (not S.isEmpty() and (precedence[S.peek()] >= precedence[cha])):
            ans += S.peek()
            S.pop()
        S.push(cha)

        
print('Postfix : ', end='')
print(ans, end='')
while not S.isEmpty():
    print(S.pop(), end='')

# print()