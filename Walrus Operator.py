# Walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# e.g 1
# happy = True
# print(happy)

# Walrus
# print(happy := True)

#------------------------------------
# e.g 2
# foods = list()
#
# while True:
#     food = input("Enter food u like: ")
#     if food == "quit":
#         break
#     foods.append(food)

# Walrus
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)



