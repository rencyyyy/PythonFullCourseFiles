# sort() method = used with lists
# sort() function = used with iterables

# Sort method: Sorts the list in alphabetical order
students = ["Anne", "Barbie", "Charlie", "Dante", "Emilio"]

students.sort()
# students.sort(reverse=True) # sort alphabetically but in reversed order

for student in students:
    print(student)

# Sort function: Sorts the list in alphabetical ordered

employees = ["Rency", "Jose", "Pedro", "Angelica", "Gon"]

sorted_employees = sorted(employees)
# sorted_employees = sorted(employees, reverse=True) # sort a list by using a function sorted (reversed order)
for i in sorted_employees:
    print(i)