# Inheritance - Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent) | sub(Super)

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def is_eating(self):
        print(f"{self.name} is eating")

    def is_sleeping(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def sound(self):
        print("ARF ARF ARF!")

class Cat(Animal):
    def sound(self):
        print("Meow Meow Meow!")

class Mouse(Animal):
    def sound(self):
        print("EeeK! eeeEk! EeeKK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.is_eating()
dog.is_sleeping()
dog.sound()

# print(cat.name)
# print(cat.is_alive)
# cat.is_eating()
# cat.is_sleeping()
# cat.sound()
#
# print(mouse.name)
# print(mouse.is_alive)
# mouse.is_eating()
# mouse.is_sleeping()
# mouse.sound()

