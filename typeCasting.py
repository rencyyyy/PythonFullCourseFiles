#Typecasting - the process of converting a variable from one data type to another.
#              str(), int (), float(), bool()

name = "Rency"
empty_name = ""
age = 21
gwa = 1.75
is_student = True

print(type(name))
print(type(age))
print(type(gwa))
print(type(is_student))
print()

gwa = int(gwa)                  #float to integer
print(gwa)
age = float(age)                #integer to float
print(age)
age = str(age)                  #integer to string
print(age)
print(type(age))
name = bool(name)               #string to boolean. And if the variable is empty, then its false
print(name)
empty_name = bool(empty_name)   #string to boolean
print(empty_name)

