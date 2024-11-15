# List comprehension - A concise way to create list in python
#                      Compact and easier to read than traditional loops
#                      [expression FOR value IN ITERABLE of condition]

# Normal way
doubles = []
for x in range(1,11):
    doubles.append(x * 2) # 1 * 2 = OUTPUT, 2 * 2 = OUTPUT, 3 * 2 = OUTPUT, 4 * 2 = OUTPUT, 5 * 2 = OUTPUT
print(doubles)

#List Comprehension
doubles = [x * 2 for x in range(1,11)] # 1 * 2 = OUTPUT, 2 * 2 = OUTPUT, 3 * 2 = OUTPUT, 4 * 2 = OUTPUT, 5 * 2 = OUTPUT... --> 10
triples = [y * 3 for y in range(1,11)] # 1 * 3 = OUTPUT, 2 * 3 = OUTPUT, 3 * 3 = OUTPUT, 4 * 3 = OUTPUT, 5 * 3 = OUTPUT... --> 10
squares = [z * z for z in range(1,11)] # 1 * self = OUTPUT, 2 * self = OUTPUT, 3 * self = OUTPUT, 4 * self = OUTPUT, 5 * self = OUTPUT... --> 10
print(doubles)
print(triples)
print(squares)

# WORK WITH STRINGS

students = ["Rency", "Justine", "Timothy", "Pau", "Franky"]
students = [student.upper() for student in students]
print(students)

#ALTERNATIVE
students = [student.upper() for student in ["Rency", "Justine", "Timothy", "Pau", "Franky"]]
print(students)

#Get every first letter of the fruit inside the list
fruits = ["Apple", "Banana", "Coconut", "Durian"]

fruits_first_char = [fruit[0] for fruit in fruits]
print(fruits_first_char)
for i in fruits_first_char:
    print(i, end=" ")
print()


# WORK WITH CONDITIONS

numbers = [1, -4, 4, -5, 6, 3, -8, 2, 10, -9]

positive_num = [num for num in numbers if num >= 0] # The "num" before for loop is a return value
print(positive_num)

negative_num = [num for num in numbers if num < 0]
print(negative_num)

even_num = [num for num in numbers if num % 2 == 0]
print(even_num)

odd_num = [num for num in numbers if num % 2 == 1]
print(odd_num)

# Check if grade is pass or failed PASSING SCORE 75 <

grades = [72, 94, 75, 86, 79, 96, 99, 89, 71, 69, 65]
passing_grade = [grade for grade in grades if grade >= 75]
print(f"PASSING GRADES IS: {passing_grade}")

fail_grade = [grade for grade in grades if grade < 75]
print(f"FAILED GRADE: {fail_grade}")




