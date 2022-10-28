def merge_sort(input_array):
    counter = 0

    if len(input_array) <= 1:
        return input_array, counter

    left = merge_sort(input_array[:len(input_array) // 2])
    right = merge_sort(input_array[len(left[0]):])

    counter += left[1] + right[1]

    left_index = 0
    right_indx = 0
    final_ndx = 0

    while left_index < len(left[0]) and right_indx < len(right[0]):
        counter += 1
        if left[0][left_index] < right[0][right_indx]:
            input_array[final_ndx] = left[0][left_index]
            left_index += 1
        else:
            input_array[final_ndx] = right[0][right_indx]
            right_indx += 1
        final_ndx += 1

    while left_index < len(left[0]):
        input_array[final_ndx] = left[0][left_index]
        left_index += 1
        final_ndx += 1
        

    while right_indx < len(right[0]):
        input_array[final_ndx] = right[0][right_indx]
        right_indx += 1
        final_ndx += 1
        

    return input_array, counter

print(" *** Merge sort ***")
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
temp = merge_sort(A)
print()
print("Sorted ->",str(temp[0]).replace("[","").replace("]","").replace(",",""))
print("Data comparison = ",temp[1])