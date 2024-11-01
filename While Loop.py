# While Loop - execute some code WHILE some condition remains trur

name = input("Enter your name: ")

while name == "":
    print()
    print("You didn't enter your name")
    name = input("Enter your name please: ")
print(f"Hello {name} kupal")

#------------------------------------------------------------------------------------------------------------------

age = int(input("Enter your age: "))

while age < 0:
    print("age can't be negative")
    age = int(input("Enter your real age: "))
print(f"You are {age} year/s old")

#------------------------------------------------------------------------------------------------------------------

girlfriend = input("Enter your girlfriend name (type quit to stop): ")

while not girlfriend == "quit":
    print(f"Your girlfriend is {girlfriend}")
    girlfriend = input("Enter another girlfriend (type quit to stop): ")

print("Thanks, bye!")

#------------------------------------------------------------------------------------------------------------------
import time
num = int(input("Enter a number between 1 to 20: "))

while num < 0 or num > 20:
    print(f" The {num} is invalid")
    num = int(input("ENTER A NUMBER BETWEEN 1 to 20!: "))

print(f"Okay you will die after {num} seconds")

for countdown in range (num,0,-1):
    print(countdown)
    time.sleep(1)
print(f"Just kidding {name}, your girlfriends loves u")



