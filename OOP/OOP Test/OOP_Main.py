#IMPORTING CLASS FROM DIFFERENT PYTHON FILE

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
#MULTIPLE AND MULTILEVEL INHERITANCE

# class Human:
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.breathing = True
#
#     def eat(self):
#         print(f"{self.name} is eating a food")
#     def sleep(self):
#         print(f"{self.name} is asleep")
#
# class front_Dev(Human):
#
#     def UserInterface(self):
#         print(f"{self.name} developing a user interface of a website")
#
#
# class back_Dev(Human):
#
#     def functions_behind(self):
#         print(f"{self.name} developing a backend of a website")
#
# class full_dev(front_Dev, back_Dev):
#     def connection(self):
#         print(f"{self.name} making connection between frontend, server and database connection")
#
# front_end_Dev = front_Dev("Rency D",21,"Male",)
# back_end_Dev = back_Dev("Justine S", 21,"Male")
# full_stack_Dev = full_dev("Justine B", 21, "Male")
#
# print(front_end_Dev.name)
# print(front_end_Dev.age)
# print(front_end_Dev.gender)
# print(front_end_Dev.breathing)
# front_end_Dev.eat()
# front_end_Dev.sleep()
# front_end_Dev.UserInterface()
# print()
# print(back_end_Dev.name)
# print(back_end_Dev.age)
# print(back_end_Dev.gender)
# print(back_end_Dev.breathing)
# back_end_Dev.eat()
# back_end_Dev.sleep()
# back_end_Dev.functions_behind()
# print()
# print(full_stack_Dev.name)
# print(full_stack_Dev.age)
# print(full_stack_Dev.gender)
# print(full_stack_Dev.breathing)
# full_stack_Dev.eat()
# full_stack_Dev.sleep()
# full_stack_Dev.UserInterface()
# full_stack_Dev.functions_behind()
# full_stack_Dev.connection()


#-----------------------------------------------------------------------------------------------------------------------
# SUPER FUNCTION
# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def description(self):
#         print(f"This shape is color {self.color} and {"filled" if self.is_filled else "not filled"}")
# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius
#     def description(self):
#         super().description()
#         print(f"The circumference of a circle is {3.14 * pow(self.radius, 2)}cm^2")
# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width
#     def description(self):
#         super().description()
#         print(f"The size of a square is {self.width * self.width}cm^2")
# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
#     def description(self):
#         super().description()
#         print(f"The size of a square is {self.width * self.height / 2}cm^2")
#
# circle = Circle(color="Red", is_filled=False, radius=5)
# square = Square(color="Blue", is_filled=True, width=7)
# triangle = Triangle(color="Yellow", is_filled=False, width=7, height=8)
#
# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)
# circle.description()
# print()
# print(square.color)
# print(square.is_filled)
# print(square.width)
# square.description()
# print()
# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)
# triangle.description()

#-----------------------------------------------------------------------------------------------------------------------\
# # DUCK TYPING
#
# class Vehicle:
#     have_license = True
#
# class Car(Vehicle):
#     def drive(self):
#         print("The car is accelerating")
#
# class Motorcycle(Vehicle):
#
#     def drive(self):
#         print("The motorcycle is accelerating")
# class Bike:                             # THIS CLASS MUST MEET OR HAVE ATTRIBUTES AND METHOD OF EVERY CLASS
#     have_license = False                # SO THAT IT BE CONSIDERED BELONG TO THE VEHICLE OBJECT
#                                         # IF NOT - THEN U MUST NOT ADD IT TO VEHICLE OBJECT BELOW.
#     def drive(self):
#         print("The man is moving using a bike")
#
#     # def padyak(self):                 # ORIGINAL METHOD
#     #     print("The man is moving using a bike")
#
# vehicles = [Car(),Motorcycle(), Bike()] # OBJECT = vehicles
#
# for vehicle in vehicles:
#     vehicle.drive()
#     print(vehicle.have_license)

#-----------------------------------------------------------------------------------------------------------------------
# CLASS METHOD
# class Student:
#
#     count = 0
#     total_average = 0
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_average += gpa
#
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
#
#     @classmethod
#     def get_count(cls):
#         return f"The total # of student is {Student.count}"
#
#     @classmethod
#     def get_total_average(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Total average {Student.total_average / Student.count:.2f}"
#
#
# student1 = Student(name="Rency", gpa=1.5)
# student2 = Student(name="Jose", gpa=1.0)
# student3 = Student(name="Blumentritt", gpa=1.2)
# student4 = Student(name="Paciano", gpa=1.4)
#
# # print(Student.get_info(student3))
# print(Student.get_count())
# print(Student.get_total_average())

#-----------------------------------------------------------------------------------------------------------------------

# Class Method
# class Student:
#     stud_count = 0
#     total_average = 0
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.stud_count += 1
#         Student.total_average += gpa
#
#     def get_info(self):
#         return f"Student name: {self.name} | GPA: {self.gpa}"
#
#     @classmethod
#     def get_count(cls):
#         return f"The total number of students: {Student.stud_count}"
#
#     @classmethod
#     def get_average(cls):
#         if cls.stud_count == 0:
#             return 0
#         else:
#             return f"The total average of {Student.stud_count} students is {Student.total_average / Student.stud_count:.2f}"
#
# student1 = Student(name="Rency Delos Santos", gpa=1.25)
# student2 = Student(name="Jose Rizal", gpa=1.00)
# student3 = Student(name="Elon Musk", gpa=1.10)
#
# print(Student.get_info(student2))
# print(Student.get_count())
# print(Student.get_average())

#-----------------------------------------------------------------------------------------------------------------------

# MAGIC METHOD
# class Book:
#
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
#
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
#
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author    # TRUE
#
#       # return self.title == other.title and self.author == other.author    # FALSE
#
#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
#
#     def __gt__(self, other):
#         return self.num_pages > other.num_pages
#
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
#
#     def __getitem__(self, item):
#         if item == "Title":
#             return self.title
#         if item == "Nag sulat":
#             return self.author
#         if item == "Bilang ng pahina":
#             return self.num_pages
#
# book1 = Book("Noli Me Tangere","Jose Rizal", 400)
# book2 = Book("El Filibusterismo","Jose Rizal", 350)
# book3 = Book("Buhat at mga Sulat ni Rizal","Jose P. Santos", 450)
#
# # print(book1) #<__main__.Book object at 0x00000243EB59D640>
#
# # __str__
# print(book1)
# print(book2)
# print(book3)
#
# # __eq__
# print(book1 == book2)
#
# # __lt__
# print(book2 < book3)
#
# # __gt__
# print(book1 > book3)
#
# # __contains__
# print("El Filibusterismo" in book1)
# print("El Noli" in book3)
# print("Jose Rizal" in book3)
#
# # __getitem__
# print(book1["Title"])
# print(book1["Nag sulat"])
# print(book1["Bilang ng pahina"])
#
# print(book2["Title"])
# print(book2["Nag sulat"])
# print(book2["Bilang ng pahina"])
#
# print(book3["Title"])
# print(book3["Nag sulat"])
# print(book3["Bilang ng pahina"])

# #-----------------------------------------------------------------------------------------------------------------------
#
# class Rectangle:
#
#     def __init__(self, width,height):
#         self._width = width
#         self._height = height
#
#     # GETTER
#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"
#
#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
#
#     # SETTER
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")
#
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._width = new_height
#         else:
#             print("Height must be greater than zero")
#
#     @width.deleter
#     def width(self):
#         del self._width
#         print("The width is deleted")
#
#     @height.deleter
#     def height(self):
#         del self._height
#         print("The height is deleted")
#
# rectangle = Rectangle(10,20)
#
# del rectangle.width
# del rectangle.height
# print(rectangle.width)
# print(rectangle.height)

#-----------------------------------------------------------------------------------------------------------------------

# # DECORATOR
#
# def add_recognition(func):
#     def wrapper(*args, **kwargs):
#         print("Cum Laude 🎓")
#         func(*args, **kwargs)
#     return wrapper
# def add_honors(func):
#     def wrapper(*args, **kwargs):
#         print("Dean's List 🐐")
#         func(*args, **kwargs)
#     return wrapper
# @add_recognition
# @add_honors
# def get_diploma(name):
#     print(f"Diploma received by: {name} 📃")
#
# get_diploma("Rency")

#-----------------------------------------------------------------------------------------------------------------------

# def addHonor(func):
#     def wrapper(*args, **kwargs):
#         print("CUM LAUDE SA PANAGINIP 📃")
#         func(*args, **kwargs)
#     return wrapper
#
# def addRecognition(func):
#     def wrapper(*args, **kwargs):
#         print("Best in wala ⭐")
#         func(*args, **kwargs)
#     return wrapper
# @addHonor
# @addRecognition
# def Graduate(name, university, program, year):
#     print(f"{name} is graduated at {university}, of {program} in {year}")
#
# Graduate("Rency","PUP Bataan","BSIT",2025)

#-----------------------------------------------------------------------------------------------------------------------


