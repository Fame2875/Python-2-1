class translator:

    def deciToRoman(self, num):

        ### Enter Your Code Here ###
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        i = 12
        roman_numresult = ''
        while num != 0:
            if numbers[i] <= num:
                roman_numresult += roman[i]
                num = num - numbers[i]
            else:
                i -= 1 #i = i - 1    
        return roman_numresult        
    def romanToDeci(self, s):
        dic ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        curr = 0
        prev = 0
        for i in range(len(s)):
            curr =dic[s[i]]
            if curr > prev:
                total = total + curr-2*prev
            else:
                total += curr

            prev = curr
        return total        
        


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))
