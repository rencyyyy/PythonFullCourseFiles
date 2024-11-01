# input () - A function that prompts the user to enter data
#            Returns the entered data as string

# name = input("Enter your name: ")
# age = int(input("Write your age last year: "))
# age += 1
# print(f"Hello, {name}")
# print(f"You are {age} years old")
# print(type(age))

# Exercise 1 - Rectangle Area Calc
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
area = length * width

print(f"The area of the rectangle is {area}cm²")          # numLock + Alt + 0178 = ² (power)
print()
# Exercise 2 - Shopping Cart Program
item = input("What item do you want to buy?: ")
price = float(input("How much is this item?: "))
quantity = int(input("How many items that you want to buy?: "))
total = price * quantity
print()
print(f"You have bought {quantity} x {item}/s")
print(f"Please pay: ₱{total}")


item = input("Enter item to buy: ")
price = float(input("How much is this item: "))
quantity = int(input(f"How many {item} that you want to buy: "))
print()
total = quantity * price
print(f"ITEM: {item}")
print(f"THE TOTAL PRICE IS P{total:.2f}")