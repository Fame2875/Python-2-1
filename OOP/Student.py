class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade 
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name , max_students):
        self.name = name
        self.max_students = max_students
        self.student = []
    
    def add_student(self,student):
        if len(self.student)  < self.max_students:
              self.student.append(student)
              return True
        return False
    
    def get_average_grade(self):
       value = 0
       for student in self.student:
           value += student.get_grade()

       return value / len(self.student)
           
         
       

s1 = Student("Tim" , 19 , 95)
s2 = Student("Bill" , 19 , 75)
s3 = Student("Jill" , 19 , 65)

c = Course("WORK", 3)
c.add_student(s1)
c.add_student(s2)
c.add_student(s3)
print(c.student[0].name)
print(c.student[1].name)
print(c.get_average_grade())