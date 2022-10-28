def findMax(a):
    if len(a) == 1:
        return a[0]
    else:
        return max(a[0],findMax(a[1:]))
arr =[int(i) for i in input("Enter Input : ").split(" ")]            
print("Max :",findMax(arr))