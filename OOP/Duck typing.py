# DUCK TYPING - Another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quack like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:                              # Class must have same methods and attributes so that it could be considered as
                                        # One of them (list of classes)
    alive = False
    def speak(self):
        print("HONK!")

    # def horn(self):
    #     print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

