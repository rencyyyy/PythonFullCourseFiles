# Membership operators - used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

#-----------------------------------------------------------------------------------------------------------------------

# INPUT - NOT IN
email = input("Enter your email: ")

if "@" not in email or "." not in email:
    print(f"{email} is not a valid email")
else:
    print(f"WELCOME {email}")

# STRING VARIABLE - IN

fruit = "BANANA"

guess = input("guess a letter: ")
if guess in fruit:
    print(f" The letter {guess} was found in the fruit")
else:
    print(f"{guess} was not found")


#-----------------------------------------------------------------------------------------------------------------------
# LIST - NOT IN

list = ["Apple", "Banana", "Orange", "Coconut"]

pick = input("Pick a fruit: ").capitalize()

if pick not in list:
    print(f"The {pick} fruit is not on the list")
else:
    print(f"The {pick} fruit was found in list")

#-----------------------------------------------------------------------------------------------------------------------
#TUPLE - IN

tuple = (1,3,5,7,10)

chooseNum = int(input("Guess a number: "))

if chooseNum in tuple:
    print(f"{chooseNum} was found in the tuple")
else:
    print(f"{chooseNum} was not in the tuple")

#-----------------------------------------------------------------------------------------------------------------------
# SET - NOT IN
set = {"Car", "Boat", "Motorcycle"}

vehicle = input("Enter vehicle: ").capitalize()

if vehicle not in set:
    print(f"{vehicle} was not on the set")
else:
    print(f"{vehicle} in the set")

#-----------------------------------------------------------------------------------------------------------------------
# DICTIONARY - NOT IN

grade_dictionary = {"Rency D.": "S-",
              "Justine B.": "S+",
              "Justine S.": "S",
              "Jefferson A.": "S+",
              "Rheniel P.": "S-",
              "Timothy V.": "S-",
              "Jimver Pol D.": "A-",
              "Rick B.": "A",
              "Sachie M.": "A+",
              "Jellamae E.": "B",
              }

student = input("Enter name of the student: ")

if student not in grade_dictionary:
    print(f"{student} not found")
else:
    print(f"STUDENT: {student} grade was {grade_dictionary[student]}")

#NOTE! Case sensitive even u use .lower(), or .upper(), or .capitalized() method in input (avoid)


#-----------------------------------------------------------------------------------------------------------------------
# ERROR!: argument of type 'int' is not iterable
# number = 12345
#
# guessNum = int(input("Guess a random number: "))
#
# if guessNum in number:
#     print(f"{guessNum} was found in the int")
# else:
#     print(f"{guessNum} was not found in the int")
#
# # ERROR!: argument of type 'int' is not iterable
# for i in number:
#     print(i)