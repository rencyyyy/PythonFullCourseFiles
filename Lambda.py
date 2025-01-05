# LAMBDA FUNCTION - Function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# lambda parameters:expression

# Normal:
# def multiply(x):
#     return x * 2
#
# print(multiply(10))

# Lambda function:
multiply = lambda x: x*2
print(multiply(10))

two_num = lambda x, y: x * y
print(two_num(30, 2))

add_three = lambda x, y, z: x + y + z
print(add_three(1, 2, 3))

full_name = lambda firstname, lastname: firstname+" "+lastname
print(full_name("Rency","Delos Santos"))

my_name = lambda first, last: f"{first} {last}"
print(my_name("Rency","Celestino"))

check_age = lambda age: True if age >= 18 else False
print(check_age(17))

