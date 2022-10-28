def insertion_sort(array):
    if (len(array) == 1):
        return
    k = 0
    for i in range(1, len(array)):
        j = i
        k += 1
        while (j > 0 and array[j - 1] > array[j]):
            if j != i:
                k += 1
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array,k


print(" *** Insertion sort ***")
list = list(map(int, input("Enter some numbers : ").split(" ")))
ans, count = insertion_sort(list)
print()
print(ans)
print("Data comparison =  {}".format(count))
