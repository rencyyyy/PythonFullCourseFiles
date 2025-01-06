# sort() method = used with lists
# sort() function = used with iterables
# REVERSE NOTE: sort method: sort(reverse=True)
#               sort function: object = sorted(list, reverse=True)
#
# LEVEL 1
print("\nLEVEL 1")
#-----------------------------------------------------------------------------------------------------------------------
# Sort method: Sorts the list in alphabetical order
print("\nSort Method")
students = ["Anne", "Barbie", "Charlie", "Dante", "Emilio"]

students.sort()
# students.sort(reverse=True) # sort alphabetically but in reversed order

for student in students:
    print(student)

# Sort function: Sorts the list in alphabetical ordered
print("\nSort function")

employees = ["Rency", "Jose", "Pedro", "Angelica", "Gon"]

sorted_employees = sorted(employees)
# sorted_employees = sorted(employees, reverse=True) # sort a list by using a function sorted (reversed order)
for i in sorted_employees:
    print(i)


# LEVEL 2
print("\nLEVEL 2")
#-----------------------------------------------------------------------------------------------------------------------

# List of tuples

players = [("Ryukaji", "A", 72),
           ("Nard", "B", 70),
           ("Albert", "C", 64),
           ("Blood", "D", 58),
           ("Cyren", "C", 60)]
# Sort method
print("\nSort by name (normal)")
players.sort()
# players.sort(reverse=True)
for i in players:
    print(i)

# Sort based on skill level (2nd index the list)
print("\nSort based on skill level")
skill_level = lambda level: level[1]
players.sort(key=skill_level)

for i in players:
    print(i)

# Sort based on KD ratio (3rd index of the list)
print("\nSort based on skill KD Ratio percentage (reversed)")
kd = lambda ratio:ratio[2]
players.sort(key=kd, reverse=True)

for i in players:
    print(i)

# Tuples of tuples
print("\nSORT TUPLES OF TUPLES BASED ON KD RATIO (reversed)")
players = (("Ryukaji", "A", 72),
           ("Nard", "B", 70),
           ("Albert", "C", 64),
           ("Blood", "D", 58),
           ("Cyren", "C", 60))

# Sort tuples of tuples based on KD Ratio
kd_ratio = lambda rate: rate[2]
sorted_player = sorted(players, key=kd_ratio, reverse=True)

for i in sorted_player:
    print(i)


