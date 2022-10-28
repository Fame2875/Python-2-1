class Pet:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} year old")

class Cat(Pet):
  
    def speak(self):
        print("Meow")
     
class Dog(Pet):
  
    def speak(self):
        print("bark")
    
p = Pet("tim", 19)   
p.show()
c = Cat("MAN", 34)
c.show()
c.speak()
d = Dog("OO", 5)
d.show()
d.speak()