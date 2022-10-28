
def findTriplets(arr, n):
    found = False
    for i in range(n - 1):
 
        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                result.append([arr[i], x, arr[j]])
                #print(arr[i], x, arr[j])
                found = True
            else:
                s.add(arr[j])
    
 
# Driver Code
arr = [int(i) for i in input("Enter Your List : ").split()]
n = len(arr)
result = [] 
if n < 3:
 print("Array Input Length Must More Than 2")  
else: 
 findTriplets(arr, n)
 result = list(set(map(tuple, result)))
 result.reverse()
 real = [[] for m in range(len(result))]
 for b in range(len(result)):
        for c in range(len(result[b])):
            real[b].append(result[b][c])
 print(real) 