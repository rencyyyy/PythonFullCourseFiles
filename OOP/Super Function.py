class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"The shape is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color,is_filled, radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"The area of a circle is {3.14 * pow(self.radius, 2)}cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"The square is {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"The area of a triangle is {self.width * self.height / 2}cm^2")

circle = Circle(color="Red",is_filled=True,radius=5)
square = Square(color="Blue",is_filled=False, width=6)
triangle = Triangle(color="Green",is_filled=False, width=7, height=8)

print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()
print()

print(square.color)
print(square.is_filled)
print(square.width)
square.describe()
print()

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
triangle.describe()
print()
