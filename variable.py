#VARIABLE - A container for a value (string, integer, float, boolean)
#           A variable behaves as if it was the value it contains

#Strings
first_name = "Rency"
last_name = "Delos Santos"
full_name = (first_name + " " + last_name)
food = "Banana"
email = "rencydelossantos020@gmail.com"
print(f"Hello {first_name}")
print(f"My name is {first_name} and my favorite food is {food}")
print(f"My email is {email}")
print(f"My name is {full_name}")

#Integer
age = 21
quantity = 5
food = 4.5
print(f"I am {age} years old")
print(f"I want to have a {quantity} books")

#Float
price = 10.99
GPA = 1.75
distance = 8.4
print(f"The price is P{price}")
print(f"My GPA is {GPA}")
print(f"The distance between my home going to my school is {distance}km")

#Boolean
is_student = True
for_sale = False
is_online = True


print(f"Are you a student: {is_student}")
if is_student:
    print("You are student")
else:
    print("You are not student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are ONLINE")
else:
    print("YOu are OFFLINE")