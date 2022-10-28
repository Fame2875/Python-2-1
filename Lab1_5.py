
x = int(input("Enter Input : "))
count = x+2
# firstline
for j in range(1, x+3, 1):
    for i in range(x+2-j):
        print(".", end='')
    for i in range(j):
        print("#", end='')

    for i in range(x+2):
        #print(i, end='')
        if i == 0 or i == x+1:
            print("+", end='')

        elif i < x+1 and j != x+2 and j != 1:
            print("#", end='')
        elif j == x+2 or j == 1:
            print("+", end='')
    print("")
for i in range(x+2):
    print("#", end='')
for i in range(x+2):
    print("+", end='')
print("")
for j in range(1, x+2, 1):
    for i in range(x+2):
        #print(i, end='')
        if i == 0 or i == x+1:
            print("#", end='')

        elif i < x+1 and j != x+1:
            print("+", end='')
        elif j == x+1:
            print("#", end='')
    print("+", end='')
    for i in range(x+1-j):
        print("+", end='')
    for i in range(j):
        print(".", end='')            
    print("")
   