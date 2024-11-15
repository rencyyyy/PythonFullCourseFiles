# Multiple inheritance - inherit from more than one parent class
#                       C(A, B)

# Multilevel inheritance - inherit from a parent which inherits from another paren
#                       C(B) <- B(A) <- A

# MULTIPLE INHERITANCE
class Prey:                         # PARENT CLASS
    def flee(self):
        print("This animal is running from its predator")

class Predator:                     # PARENT CLASS
    def hunt(self):
        print("This animal is chasing its prey")

class Lion(Predator):               # CHILD CLASS (Predator)
    pass

class Snake(Predator, Prey):        # CHILD CLASS (Prey, Predator)
    pass

class Rabbit(Prey):                 # CHILD CLASS (Prey)
    pass

lion = Lion()           #OBJECT
snake = Snake()         #OBJECT
rabbit = Rabbit()       #OBJECT

lion.hunt()
snake.hunt()
snake.flee()
rabbit.flee()


#MULTILEVEL INHERITANCE

class Student:                              # GRAND PARENT CLASS

    def __init__(self, name):               # Constructor in Grand Parent (Student Class)
        self.name = name

    def studying(self):
        print(f"{self.name} is studying")
    def doing_assignment(self):
        print(f"{self.name} is doing its assignment")

class Boy(Student):                         # PARENT CLASS
    def doing_programming(self):
        print(f"{self.name} is programming")

class Girl(Student):                        # PARENT CLASS
    def doing_design(self):
        print(f"{self.name} is designing")

class Rency(Boy):
    pass

class Sachie(Boy, Girl):
    pass

class Angelica(Girl):
    pass

rency = Rency("Rency")
sachie = Sachie("Sachie")
angelica = Angelica("Angelica")


# There's Access in Grandparent Class
rency.studying()
rency.doing_programming()
rency.doing_assignment()
# There's no access in Girl Parent class

# There's Access in Grandparent Class
sachie.studying()
sachie.doing_assignment()
sachie.doing_programming()
sachie.doing_design()
# Has access bot Boy and Girl Parent Class

# There's Access in Grandparent Class
angelica.studying()
angelica.doing_assignment()
angelica.doing_design()
# There's no access in Boy Parent Class

#NOTE! ALL OF THEM HAS ACCESS IN (STUDENT) GRANDPARENT BECAUSE BOTH PARENT CLASS (BOY & GIRL) INHERIT IT
# THE CONSTRUCTOR NAME ARE IN GRANDPARENTS SO THEY HAVE ALL ACCESS IN NAME. THROUGH ASSIGNING NAME IN THEIR OBJECT.






