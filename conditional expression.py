#Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two vales based on a condition
#                         X if condition else Y

# Check if the number is positive or negative number
num = -2
print("The number is positive" if num >= 0 else "The number is negative")

# Check if the number is even or odd

print("The number is even number" if num % 2 == 0 else "The number is odd number")


# Check the lower or higher number between 2 variables, print their output
a = 6
b = 3

max_num = a if a > b else b
min_num = a if a < b else b
print(f"The {max_num} is greater than the others")
print(f"The {min_num} is lower than others")

# Check if the person is adult or not

age = 17
result = "You are adult" if age >=18 else "You are not adult yet"
print(result)

# Check if the temperature is warm or hot
weather = 40
weather = "The temperature is HOT" if weather >= 30 else "The temperature is warm"
print(weather)

# Check the access of the user

user_access = "admin"

access_level = "Full access" if user_access == "admin" else "Access denied"
print(access_level)





