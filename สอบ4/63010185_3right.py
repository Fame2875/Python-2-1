
def insertsort(arr):
    k = 0
    if len(arr) == 1:
        return
     
    for i in range(1, len(arr)):
      k += 1
      j = i
      while(j > 0 and arr[j - 1] > arr[j]):
          if j != i :
            k += 1
          arr[j], arr[j-1]  = arr[j-1], arr[j]
    return arr , k      
          





print(" *** Insertion sort ***")
lst = [int(i) for i in input('Enter Input : ').split()]
print("")
ans , count =insertsort(lst)
print(ans)
print("Data comparison =",count)
