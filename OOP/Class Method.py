# CLASS METHODS - Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility function that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_average = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_average += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"The total # of student is {Student.count}"

    @classmethod
    def get_total_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Total average {Student.total_average / Student.count:.2f}"


student1 = Student(name="Rency", gpa=1.5)
student2 = Student(name="Jose", gpa=1.0)
student3 = Student(name="Blumentritt", gpa=1.2)
student4 = Student(name="Paciano", gpa=1.4)

# print(Student.get_info(student3))
print(Student.get_count())
print(Student.get_total_average())