h,w = input("Enter your High and Weight : ").split()
bmi = float(w)/ (float(h)**2)
if bmi < 18.50:
    print("Less Weight")
elif bmi < 23:
    print("Normal Weight")
elif bmi < 25:
    print("More than Normal Weight")   
elif bmi < 30: 
    print("Getting Fat")  
else:
    print("Fat")
 