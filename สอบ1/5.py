
class MyInt:
    def __init__(self,num):
        self.num = num
        self.number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        self.roman =['I', 'IV', 'V', 'IX', 'X', 'XL',
            'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    def toRoman(self):
        num =self.num

        numbers = self.number
        roman = self.roman
        i = 12
        roman_numresult = ''
        while num != 0:
                if numbers[i] <= num:
                    roman_numresult += roman[i]
                    num = num - numbers[i]
                else:
                    i -= 1  
        return roman_numresult
    def __add__(self):
        return self.num*1.5    
    

#r1 =Roman(500)
#print(r1.toRoman())
print(" *** class MyInt ***")
a,b = input("Enter 2 number : ").split(" ")
a = int(a)
b = int(b)
r1 =MyInt(a)
r2 =MyInt(b)
# print(r1.toRoman())
print(a,"convert to Roman :",r1.toRoman())
print(b,"convert to Roman :",r2.toRoman())
print(a,"+",b,"=",int(r1.__add__()+r2.__add__()))
