from OOP_Import import *
student1 = Student(1,"Rency",21,"1-BSIT",4,"Male")
student2 = Student(2,"Angelica",21,"1-BSIT",4,"Female")


print(f"The number of students are {Student.num_of_Student}")
print(student1.id)
student1.is_present()

print(student2.id)
student2.is_absent()

print(f"Hello, my name is {student1.name} I am {student1.age} years old")
print(f"I am {student1.year}th year student from {student1.section} and I am {student1.gender}")

