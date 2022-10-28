class funString():

    def __init__(self,string = ""):

        ### Enter Your Code Here ###
        self.string = string

    def __str__(self):
       copy = self.string
        ### Enter Your Code Here ###
       return (len(self.string))

    def size(self) :

        copy = self.string
        ### Enter Your Code Here ###
        return (len(self.string))


    def changeSize(self):

        copy = self.string
        temp = ""
        for i in copy:
            if (ord(i) >= 97):
                temp += chr(ord(i) - 32)
            elif(ord(i) >= 65):
                temp += chr(ord(i) + 32)
        return(temp)

    def reverse(self):

        ### Enter Your Code Here ###
        copy = self.string
        temp = ""
        for i in range(len(copy)):
            temp += copy[(len(copy)-1)-i]
        return(temp)

    def deleteSame(self):

       ### Enter Your Code Here ###
        copy = self.string
        temp = ""
        temp +=copy[0]
        for i in range(len(copy)-1) :
            if(not (copy[i+1] in temp)):
                temp += copy[i+1]
        return(temp)



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())
