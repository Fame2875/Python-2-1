def parenMatching(str):
    s = []
    i =0
    count =0
   # print("G",len(str))
    while i<len(str) :
       
        c =str[i]
        if c in '{[(':
            s.append(c)
        else:
            if c in '}])':
                if len(s)>0:
                    
                    if not match(s.pop(),c):    
                     count +=2
                else:
                 count +=1
        i += 1
    if len(s) > 0 :
        for i in range(len(s)):
            count +=1
    return count,c,i,s        

def match(open,close):
    return(open =='(' and close ==')') or\
     (open =='{' and close =='}')  or \
    (open =='[' and close ==']')
def match2(op,cl):
    opens ="([{"
    closes =")]}"
    return opens.index(op) == closes.index(cl) 
str= input("Enter Input : ")
counT,c,i,s =parenMatching(str)
print(counT)
if counT == 0:
    print("Perfect ! ! !")

