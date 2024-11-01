#

friends = 0

# friends = friends + 1
friends += 4            #increment / +          Output: 4
friends -= 1            #decrement / -          Output: 3
friends *= 5            #multiplied / *         Output: 15
friends **= 3           #pow (15x15x15)         Output: 3375
friends /= 15           #divide     /           Output: 225.0
remainder = friends % 10               #modulo(get the reminder when being divided into the inputed number
print(friends)
print(remainder)                       # Output: 5.0

age = 10
get = age % 3                          # #Output: 1  (Popular to use this operator to find if a number is even or odd -
print(get)                             #               because it will divide by two evenly if that number is even)
print()

#-----------------------------------------------------------------------------------------------------------------------
# Math Function

x = 1.43
y = -5
z = 3

# result = round(x)        # Round a number to the nearest integer or a specified number of decimal places. (1)
# result = abs(y)          # Absolute value is the distance away from zero as a whole number. (5)
# result = pow(z, 5)       # To compute the power of a number by raising it to a certain exponent. (243)
# result = max(x, y, z)    # To find which among the three has the highest value, (3)
# result = min (x, z, y)   # To find what value is the lowest among the three variables (-5)
# print(result)

import math

a = 9
b = 1.12
c = 2.7

print(math.pi)             # To find what is the value of a pi in math function
print(math.e)              # To find what is the exponential constant in math function
# output = math.sqrt(a)
# output = math.ceil(b)
# output = math.floor(c)
# print(output)

#Exercise 1 - Calculate the circumference of a circle (import math module) C = 2 π r

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of a circle is {round(circumference, 2)} cm")

#Exercise 2 - Calculate the area of a circle A = π r^2

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of a circle is {round(area, 2)} cm^2")

#Exercise 3 - Find the hypotenuse of a right triangle C = the square root of a squared and b squared

side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))

side_c = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
print(f"The side C is {side_c}")

#Exercise 4 - From anonymous participants Compute the volume of a sphere. V = (4/3) * pi * r^3

radius = float(input("Enter the radius of a sphere: "))
volume = (4/3) * math.pi * pow(radius, 3)
print(f"The volume of a sphere is {round(volume, 2)}")

#Exercise 5 - From anonymous participants. Convert dollar into peso. Let's assume that $1 = P51.50

dollar = int(input("How much dollar do you have?: "))
peso = 51.50
result = peso * dollar
print(f"Ang pera mo ay ₱{round(result, 2)}")














