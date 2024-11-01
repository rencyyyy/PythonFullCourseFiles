# Python Calculator


#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# operator = input("Enter operator ( + - * / ): ")
#
# if operator == "+":
#    result = num1 + num2
#    print(f"RESULT: {round(result, 2)}")
# elif operator == "-":
#     result = num1 - num2
#     print(f"RESULT: {round(result, 2)}")
# elif operator == "*":
#     result = num1 * num2
#     print(f"RESULT: {round(result, 2)}")
# elif operator == "/":
#     result = num1 / num2
#     print(f"RESULT: {round(result, 2)}")
# else:
#     print(f"{operator} is not valid operator")

#=======================================================================================================================
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operator = input("Enter operator (+ - * /): ")
result = 0
if operator == "+":
    result = num_1 + num_2
elif operator == "-":
    result = num_1 - num_2
elif operator == "*":
    result = num_1 * num_2
elif operator == "/":
    result = num_1 / num_2
else:
    print(f"The {operator} is not valid")

print(f"The result is {result}")