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