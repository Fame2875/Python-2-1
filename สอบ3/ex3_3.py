def gcd(x, y):
    if y == 0:
        return x
    elif x == 0:
        return y
    else:
        return gcd(y, x % y)


a, b = input("Enter Input : ").split(" ")
aa = int(a)
bb = int(b)

if abs(aa) == 0 and abs(bb) == 0:
    print("Error! must be not all zero.")
elif aa == 0 and bb < 0:
    print("The gcd of",aa ,"and",bb,"is :", abs(gcd(aa, bb)))
elif bb == 0 and aa < 0:
    print("The gcd of",bb ,"and",aa,"is :", abs(gcd(aa, bb)))        
elif abs(aa) < abs(bb):
    print("The gcd of",bb ,"and",aa,"is :", abs(gcd(aa, bb)))
elif abs(bb) < abs(aa):
    print("The gcd of",aa ,"and",bb,"is :", abs(gcd(aa, bb)))
elif abs(bb) == abs(aa): 
    print("The gcd of",aa ,"and",bb,"is :", abs(aa))   


