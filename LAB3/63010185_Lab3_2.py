
def parenMatching(str):
    s = []
    i =0
    error =0
   # print("G",len(str))
    while i<len(str) and error ==0:
       
        c =str[i]
        if c in '{[(':
            s.append(c)
        else:
            if c in '}])':
                if len(s)>0:
                    
                    if not match(s.pop(),c):    
                     error =1
                else:
                 error =2
        i += 1
    if len(s) > 0 and error ==0:
     error = 3
    return error,c,i,s        

def match(open,close):
    return(open =='(' and close ==')') or\
     (open =='{' and close =='}')  or \
    (open =='[' and close ==']')
def match2(op,cl):
    opens ="([{"
    closes =")]}"
    return opens.index(op) == closes.index(cl) 
str= input("Enter expresion : ")
err,c,i,s =parenMatching(str)
if err ==1:
    print(str,'Unmatch open-close')
elif err ==2:
    print(str,'close paren excess')
elif err ==3:
    print(str,'open paren excess  ',len(s),':',end=' ')
    for ele in s:
        print(ele,sep='',end='')
    print()
else:
    print(str,'MATCH')            


