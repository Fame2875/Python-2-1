class Dog:

    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    
    def add_one(self,x):
     return x + 1

    def bark(self):
        print("bark")
    def get_name(self):
      return self.name
    def get_age(self):
        return self.age  
    def set_age(self,age):
        self.age = age    
    def set_name(self,name):
        self.name = name    


d = Dog("", 1)
d.set_age(20)
d.set_name("Max")
print(d.get_name())
print(d.get_age())
d2 = Dog("Bill", 12)
print(d2.get_name())
print(d2.get_age())