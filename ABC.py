index = [int(i) for i in input("EE").split()]
string = input()
index.sort()
for letter in string:
    if letter == "A":
        print(index[0], end=" ")
    elif letter == "B":
        print(index[1], end=" ")
    else :
        print(index[2], end=" ")
        #letter == "C":