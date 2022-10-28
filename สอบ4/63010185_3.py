def insertionRecursion(array, n):
    if n <= 1:
        return
    insertionRecursion(array, n-1)
    last = array[n-1] 
    j = n - 2
    j = forLoopRecursion(array, j, last) 
    array[j+1] = last
    a = len(array)
    if len(array) != n:
        print(f'insert {last} at index {j+1} :', array[:n], array[n:])
    else:
        print(f'insert {last} at index {j+1} :', array)

def forLoopRecursion(array, j, last):
    if j < 0 or array[j] < last:
        return j

    array[j+1] = array[j] 
    return forLoopRecursion(array, j-1, last) 


lst = [int(i) for i in input('Enter Input : ').split()]

insertionRecursion(lst, len(lst))

print(lst)
print("Data comparison =")