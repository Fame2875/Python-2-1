class Stack:

    def __init__(self,arg):
        self.items = []
        self.arg = arg

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###
for char_inp in inp:

    if (char_inp >= 'A' and char_inp <= 'Z') or (char_inp >= 'a' and char_inp <= 'z'):
        strAnswer += char_inp
    elif char_inp == '(':
        S.push(char_inp)
    elif char_inp == ')':
        while S.peek() != '(':
            strAnswer += S.items[-1]
            S.pop()
        S.pop()  # pop the last '('
    else:
        while (not S.isEmpty() and (precedence[S.peek()] >= precedence[char_inp])):
            strAnswer += S.peek()
            S.pop()
        S.push(char_inp)

        
print('Postfix : ', end='')
print((strAnswer), end='')
while not S.isEmpty():
    print(S.pop(), end='')
#while not S.isEmpty():

    #print(S.pop(), end='')

#print()