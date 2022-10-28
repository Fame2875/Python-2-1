print(" *** Divisible number ***")
num = input("Enter a positive number : ")
num =int(num)
if num == 0:
    print("0 is OUT of range !!!")
else:
    i = 1
    count =0
    print("Output ==>",end=" ")
    for i in range(num+1):
        if i !=0 :
          if num % i == 0:  
            print(i,end=" ")
            count += 1
print(end="\n")            
print("Total ==>",count)
