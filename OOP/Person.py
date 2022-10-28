class Person:
    number_of_person = 0
    Gravity = -9.8
    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod
    def number_of_person_(cls)  :
        return cls.number_of_person
    @classmethod
    def add_person(cls)  :
        cls.number_of_person += 1

p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_person_())

