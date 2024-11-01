# IF Statement - Do some code only IF some condition is True
# ELSE - Do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are signed up!")
elif age <= 0:
    print("You're not been born yet")
else:
    print("You have to be at least 18 years old to sign up")

food = input("Do you want some food?: (Y/N): ")

if food == "Y":
    print("You have some food")
else:
    print("There's no food for you")

online = False

if online:
    print("You are online")
else:
    print("You are offline")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")
