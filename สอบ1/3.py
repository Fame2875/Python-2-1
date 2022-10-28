lower_list = []
upper_list = []
countl =0
countu =0
print(" *** String count ***")
string =  input("Enter message : ")
for i in string:
    if i.islower():
       if i in lower_list:
         lower_list.remove(i)   
       lower_list.append(i)
       countl +=1
    if i.isupper():
        if i in upper_list:
         upper_list.remove(i)  
        upper_list.append(i)
        countu +=1

print("No. of Upper case characters :",countu)
print("Unique Upper case characters :",end=" ")
upper_list.sort()
for i in upper_list:
    print(i,end="  ") 
print(end="\n")           
print("No. of Lower case Characters :",countl)
print("Unique Lower case characters :",end=" ")
lower_list.sort()
for i in lower_list:
    print(i,end="  ")                   
       