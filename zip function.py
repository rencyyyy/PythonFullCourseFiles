# zip(*iterables) - aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each elements

#-----------------------------------------------------------------------------------------------------------------------
print("ZIP LIST AND TUPLE")
usernames = ["patecelestino","fanthom509","kaji_6969"]
passwords = ("rency123", "rency2020", "ryu002")

users = zip(usernames, passwords)
print(type(users))

for i in users:
    print(i)

#-----------------------------------------------------------------------------------------------------------------------
print("\nZIP TUPLE AND TUPLE, change the type into a list")
usernames = ("patecelestino","fanthom509","kaji_6969")
passwords = ("rency123", "rency2020", "ryu002")

users = list(zip(usernames, passwords))
print(type(users))

for i in users:
    print(i)

#-----------------------------------------------------------------------------------------------------------------------
print("\nZIP LIST AND SETS, change the type into a dictionary")

usernames = {"patecelestino","fanthom509","kaji_6969"}
passwords = ["rency123", "rency2020", "ryu002"]

users = dict(zip(usernames, passwords))
print(type(users))

for key,value in users.items():
    print(key+" : "+value)

#-----------------------------------------------------------------------------------------------------------------------
print("\nMultiple | Combination of list, sets, tuple")

employee_name = {"Meliodas","Ban","Elizabeth"}
employee_age = (3050, 100, 18)
employee_position = ["Full Stack Dev", "Cyber Security","Quality Assurance"]

employee = zip(employee_name,employee_age,employee_position)
print(type(employee))
for i in employee:
    print(i)