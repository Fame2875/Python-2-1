'''
เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab

Enter Input a b : 5 10
9765625


'''
def power(x, y):
    if y == 0:
        return 1

    if y >= 1:
        return x * power(x, y - 1)
a,b = input("Enter Input a b : ").split(" ")
a = int(a)
b = int(b)

print(power(a, b))