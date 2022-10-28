'''
ให้เขียน Recursive หาค่า Min ของ Input

Enter Input : 8 7 10 1 5 4 2 6 3 9
Min : 1

Enter Input : -84 -230 -54845 -6 -1
Min : -54845

'''

def findMinimum(l):
    if len(l) == 1:
       return l[0]

    else:
       
       return min(l[0], findMinimum(l[1:]))
arr = [int(i) for i in input("Enter Input : ").split(" ")]
print("Min :",findMinimum(arr))