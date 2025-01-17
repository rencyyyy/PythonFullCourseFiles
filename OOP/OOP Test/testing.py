# RECALL TIME

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def describe(self):
#         print (f"This shape is color {self.color} and {"filled" if self.is_filled else "not filled"}")
# class Circle(Shape):
#
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color,is_filled)
#         self.radius = radius
#
#     def describe(self):
#         super().describe()
#         return f"The circumference of circle is {3.14 * self.radius ** 2}cm^2"
#
#
# class Square(Shape):
#
#     def __init__(self, color, is_filled, width):
#         super().__init__(color,is_filled)
#         self.width = width
#     def describe(self):
#         super().describe()
#         return f"The square is {self.width ** 2}cm^2"
# class Triangle(Shape):
#
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
#
#     def describe(self):
#         super().describe()
#         return f"The triangle is {self.width * self.height / 2}cm^2"
#
# circle = Circle("Red", True, 5)
# square = Square("Blue",False,6)
# triangle = Triangle("Green",True,7,8)
#
# print(circle.describe())
# print(square.describe())
# print(triangle.describe())

#-----------------------------------------------------------------------------------------------------------------------
# from abc import ABC, abstractmethod
#
# class Shape:
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return f"{3.14 * self.radius ** 2}"
#
# class Square(Shape):
#     def __init__(self, width):
#         self.width = width
#
#     def area(self):
#         return f"{self.width ** 2}"
# class Triangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return f"{self.width * self.height * 0.5}"
#
# class Pizza(Circle):
#     def __init__(self,radius):
#         super().__init__(radius)
#
#
#
# shapes = [Circle(4), Square(5), Triangle(6,7), Pizza(15)]
#
# for shape in shapes:
#     print(shape.area())

#-----------------------------------------------------------------------------------------------------------------------

# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")
# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")
#
# class Mice(Animal):
#     def speak(self):
#         print("EEEK!")
#
# class Car:
#     alive = False
#     def sound(self):
#         print("BROOM!")
#
#     def speak(self):
#         print("Im not speaking lol xD")
#
# animals = [Dog(), Cat(), Mice(), Car()]
# for animal in animals:
#     animal.speak()
#     print(animal.alive)

#-----------------------------------------------------------------------------------------------------------------------

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         return f"{self._width:.2f} cm"
#
#     @property
#     def height(self):
#         return f"{self._height:.2f} cm"
#
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
#             self._height = new_height
#         else:
#             print("height must be greater than zero")
#
#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width is deleted")
#
#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height is deleted")
#
# rectangle = Rectangle(5,6)
#
# del rectangle.width
# del rectangle.height

# print(rectangle.width)
# print(rectangle.height)

#-----------------------------------------------------------------------------------------------------------------------

# class Book:
#
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
#
#     def __eq__(self, other):
#         return f"{self.title == other.title or self.author == other.author}"
#
#     def __lt__(self, other):
#         return self.pages < other.pages
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
#
#     def __getitem__(self, item):
#         if item == "Pamagat":
#             return self.title
#         elif item == "Nag lagda":
#             return self.author
#         elif item == "Pahina":
#             return self.pages
#         else:
#             print("There's no such item in book objects")
#
# book1 = Book("Noli Me Tangere","Jose Rizal",340)
# book2 = Book("El Filibusterismo","Jose Rizal",400)
# book3 = Book("Buhay ni Rizal","Jose P. Santos",450)
#
# print(book1)
#
# print(book1 == book2)
#
# print(book2 < book1)
#
# print(book2 > book3)
#
# print(book2 + book3)
#
# print("Santos" in book1)
#
# print(book1["Pahina"])

#-----------------------------------------------------------------------------------------------------------------------


# def add_program(func):
#     def wrapper(*arg, **kwargs):
#         print("BSIT")
#         func(*arg, **kwargs)
#     return wrapper
# def add_year(func):
#     def wrapper(*arg, **kwargs):
#         print("4TH YEAR")
#         func(*arg, **kwargs)
#     return wrapper
# @add_year
# @add_program
# def full_name(name, surname):
#     print(f"Hi my name is {name} {surname}")
#
# full_name("Rency","Delos Santos")

#-----------------------------------------------------------------------------------------------------------------------


# class Book:
#
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
#     def __eq__(self, other):
#         return self.title == other.title or self.author == other.author
#
#     def __lt__(self, other):
#         return self.pages < other.pages
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
#     def __contains__(self, item):
#         return item in self.title or item in self.author
#
#     def __getitem__(self, item):
#         if item == "Book title":
#             return self.title
#         elif item == "Book Author":
#             return self.author
#         elif item == "Book Pages":
#             return self.pages
#         else:
#             print("There's no such item")
#
# book1 = Book(title="Noli Me Tangere", author="Jose P. Rizal", pages=400)
# book2 = Book(title="El Filibusterismo", author="Jose P. Rizal", pages=350)
# book3 = Book(title="Buhay ni Rizal", author="Jose P. Santos", pages=450)
#
# print(book1)
#
# print(book1 == book3)
#
# print(book1 < book3)
#
# print(book3 > book2)
#
# print(book3 + book2)
#
# print("Rency" in book3)
#
# print(book1["Book Author"])

#-----------------------------------------------------------------------------------------------------------------------

# class Student:
#     count = 0
#     total_gpa = 0
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#
#     def get_info(self):
#         print(f"{self.name} = {self.gpa}")
#
#     @classmethod
#     def get_count(cls):
#         print(f"The total number of students is {Student.count}")
#
#     @classmethod
#     def get_total_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             print(f"The total GWA of {Student.count} students is {Student.total_gpa / Student.count}")
#
# student1 = Student("Rency", 1.50)
# student2 = Student("Jose", 1.00)
# student3 = Student("Pedro", 1.75)
# student4 = Student("Juan", 2.75)
#
# print(student1.name)
# print(student1.gpa)
# student1.get_info()
# student2.get_info()
# Student.get_count()
# Student.get_total_gpa()

#-----------------------------------------------------------------------------------------------------------------------

# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         return f"{self.name} is '{self.position}'"
#
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Front-End", "Back-End", "Full-Stacks"]
#         return position in valid_positions
#
# employee1 = Employee("Rency", "Software Engineer")
#
# print(employee1.get_info())
# print(Employee.is_valid_position("Data Analyst"))

