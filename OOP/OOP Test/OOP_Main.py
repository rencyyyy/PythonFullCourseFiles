# from OOP_Import import *
# student1 = Student(1,"Rency",21,"1-BSIT",4,"Male")
# student2 = Student(2,"Angelica",21,"1-BSIT",4,"Female")
#
#
# print(f"The number of students are {Student.num_of_Student}")
# print(student1.id)
# student1.is_present()
#
# print(student2.id)
# student2.is_absent()
#
# print(f"Hello, my name is {student1.name} I am {student1.age} years old")
# print(f"I am {student1.year}th year student from {student1.section} and I am {student1.gender}")

#-----------------------------------------------------------------------------------------------------------------------

class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.breathing = True

    def eat(self):
        print(f"{self.name} is eating a food")
    def sleep(self):
        print(f"{self.name} is asleep")

class front_Dev(Human):

    def UserInterface(self):
        print(f"{self.name} developing a user interface of a website")


class back_Dev(Human):

    def functions_behind(self):
        print(f"{self.name} developing a backend of a website")

class full_dev(front_Dev, back_Dev):
    def connection(self):
        print(f"{self.name} making connection between frontend, server and database connection")

front_end_Dev = front_Dev("Rency D",21,"Male",)
back_end_Dev = back_Dev("Justine S", 21,"Male")
full_stack_Dev = full_dev("Justine B", 21, "Male")

print(front_end_Dev.name)
print(front_end_Dev.age)
print(front_end_Dev.gender)
print(front_end_Dev.breathing)
front_end_Dev.eat()
front_end_Dev.sleep()
front_end_Dev.UserInterface()
print()
print(back_end_Dev.name)
print(back_end_Dev.age)
print(back_end_Dev.gender)
print(back_end_Dev.breathing)
back_end_Dev.eat()
back_end_Dev.sleep()
back_end_Dev.functions_behind()
print()
print(full_stack_Dev.name)
print(full_stack_Dev.age)
print(full_stack_Dev.gender)
print(full_stack_Dev.breathing)
full_stack_Dev.eat()
full_stack_Dev.sleep()
full_stack_Dev.UserInterface()
full_stack_Dev.functions_behind()
full_stack_Dev.connection()