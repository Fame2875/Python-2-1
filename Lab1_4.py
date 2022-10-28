print("*** Fun with Drawing ***")
x = int(input("Enter input : "))

# line 1
for i in range(x-1):
    print(".", end='')
print("*", end='')
for i in range((x-2)*2+1):
    print(".", end='')
print("*", end='')
for i in range(x-1):
    print(".", end='')
print("")
for j in range(x-2, 0, -1):
    for i in range(j):
        print(".", end='')
    print("*", end='')
    for i in range((x-2-j)*2+1):
        print("+", end='')
    print("*", end='')
    for i in range(j*2-1):
        print(".", end='')
    print("*", end='')
    for i in range((x-2-j)*2+1):
        print("+", end='')
    print("*", end='')
    for i in range(j):
        print(".", end='')
    print("")
    # line n
print("*", end='')
for i in range((x-2)*2+1):
    print("+", end='')
print("*", end='')
for i in range((x-2)*2+1):
    print("+", end='')
print("*")
line = 1
p = (x-2)*4+1
while (p > 0):
    for i in range(line):
        print(".", end='')
    print("*", end='')
    for i in range(p):
        print("+", end='')
    print("*", end='')
    for i in range(line):
        print(".", end='')
    print("")
    p = p-2
    line = line+1

for i in range(line):
    print(".", end='')
print("*", end='')
for i in range(line):
    print(".", end='')
