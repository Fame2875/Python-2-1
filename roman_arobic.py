class translator:

    def deciToRoman(self, num):

        ### Enter Your Code Here ###
        count_digit = []
        num_copy = self.num
        while num_copy > 0:
         num_copy = num_copy%10
         count_digit.append(num_copy)
        count_digit.reverse()
        result =""
        number_pos =0
        #น้อยกว่า1000
        if len(count_digit) >= 4:
            num = 0
        #มากกว่า1000
        i = int    

   

    #def romanToDeci(self, s):
        


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

#print(translator().romanToDeci(translator().deciToRoman(num)))
