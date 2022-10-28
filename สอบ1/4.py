print("*** String Rotation ***")
a, b = input("Enter 2 strings : ").split(" ")
count = 1
if len(a) == len(b):
    for i in range(len(a)):
        if count < 5:
         print(count,end=" ")
         print(a[i+1:]+a[:i+1],end=" ")
         print(b[i+1:]+b[:i+1])
        count += 1
        if len(a)-5 >= count:
         print(".......")
         print(count,end=" ")
         print(a[i+1:]+a[:i+1],end=" ")
         print(b[i+1:]+b[:i+1])


if len(a) != len(b):
    x = len(a)*len(b)
    if count < 5:
         print(count,end=" ")
         print(a[i+1:]+a[:i+1],end=" ")
         print(b[i+1:]+b[:i+1])
    count += 1
    if len(a)-5 >= count:
         print(".......")
         print(count,end=" ")
         print(a[i+1:]+a[:i+1],end=" ")
         print(b[i+1:]+b[:i+1])

print("Total of ",count-1,"rounds.")