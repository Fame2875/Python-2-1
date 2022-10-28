

test_list = input("Enter Input : ").split()
test_list = [int(i) for i in test_list]
flag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1
    i += 1
      
# printing result
if (not flag) :
    print ("Yes")
else :
    print ("No")