# CLASS VARIABLE - Shared among all instances of a class
#                  Define outside the constructor
#                  Allow you to share data among all objects created from that class
class Student:

    class_year = 2021                           # Class variable
    num_of_students = 0                         # CLass variable
    def __init__(self, name, age):              #Constructor
        self.name = name
        self.age = age
        Student.num_of_students += 1            # Increment


student1 = Student("Rency",21)      #Object1
student2 = Student("Juan",21)       #Object2


print(student1.name)
print(student1.age)
print(student1.class_year)
# or print(Student.class_year) # name of class then the attributes(variable)

print(student2.name)
print(student2.age)
print(student2.class_year)     # Class variable is accessible to all the objects that created
# or print(Student.class_year) # name of class then the attributes(variable)
print(Student.num_of_students)



