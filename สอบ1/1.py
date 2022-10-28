print(" *** Wind classification ***")
speed = input("Enter wind speed (km/h) : ")
speed =float(speed)
if 0 <= speed <= 51.99:
    print("Wind classification is Breeze.")
elif 52 <= speed <= 55.99:
    print("Wind classification is Depression.")
elif 56 <= speed <= 101.99:
    print("Wind classification is Tropical Storm.")  
elif 102 <= speed <= 208.99:
    print("Wind classification is Typhoon.")
elif speed >= 209:
    print("Wind classification is Super Typhoon.")
else:
    print("!!!Wrong value can't classify.")                