choice= [str(x) for x in input("Enter Input : ").split(',') ]
re = []
for i in range(len(choice)):
   list_in = choice[i]
   x = list_in.split(' ')
   #print(len(x))
   if len(x) > 1:
      re.append(x[1])
      print("Add =",x[1],"and Size =",len(re))
     
   if len(x) == 1:
      if len(re) >0:
       print("Pop =",re.pop(),"and Index =",len(re))
      else:
         print("-1")


#print('-'.join(list_in))
#a =list_in.split(" ")


print("Value in Stack = ",end="")
if len(re) == 0:
   print("Empty")
else:
 for i in range(len(re)):
   print(re[i],end=' ')
