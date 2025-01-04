class Car:
    color = None

class Motorcycle:
    color = None
def change_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

motorcycle_1 = Motorcycle()
motorcycle_2 = Motorcycle()
motorcycle_3 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "yellow")

change_color(motorcycle_1, "orange")
change_color(motorcycle_2, "green")
change_color(motorcycle_3, "purple")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(motorcycle_1.color)
print(motorcycle_2.color)
print(motorcycle_3.color)