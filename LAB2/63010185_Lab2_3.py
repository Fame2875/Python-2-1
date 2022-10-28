def odd_even(arr, s):
    #Code Here
    mi =[]
    if type(arr) is list:
        if s == 'Odd':
            for i in range(len(arr)):
                if i % 2 == 0:
                    mi.append(arr[i])
            print(mi)            
      
        if s == 'Even':
            for i in range(len(arr)):
                if i%2 ==1:
                    mi.append(arr[i])
            print(mi)  
    
    if type(arr) is str:
        temp = ""
        
        if s == 'Odd':
            for i in range(len(arr)):
                if i % 2 == 0:
                    temp += arr[i] 
            print(temp)                    
                 
        if s == 'Even':
            for i in range(len(arr)):
                if i%2 ==1:
                    temp += arr[i]  
            print(temp)                      





    
print("*** Odd Even ***")    
x,Str,choice= input("Enter Input : ").split(',') 
if x is 'L':
   list_in = Str.split(" ")
  # print(list_in)
   odd_even(list_in,choice)
   
   
if x is 'S':
    #print(Str)
    odd_even(Str,choice)