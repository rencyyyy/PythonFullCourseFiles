# Object = a "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def is_running(self):
        print(f"The {self.model} is running")

    def not_running(self):
        print(f"The {self.model} is not running")

car1 = Car("Supra",2024,"Red",False)
car2 = Car("BMW",1990,"Blue",True)
car3 = Car("Ferrari",2021,"Red",True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.is_running()
car1.not_running()

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)
# car2.is_running()
# car2.not_running()
#
# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)
# car3.is_running()
# car3.not_running()

