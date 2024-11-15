#Logical operators - evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)

# temp = 20
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:                 # if may condition na may na meet at least 1 then i-eexecute
#     print("The event is cancelled")
# else:
#     print("The event is still scheduled")
#-----------------------------------------------------------------------------------------------------------------------
temp = 10
is_sunny = False

if temp >= 30 and is_sunny:
    print("Its hot outside")
    print("Tirik ang araw")
elif 30 > temp > 0 and is_sunny:
    print("Its warm outside")
    print("May araw sa labas")
elif 30 > temp > 0 and not is_sunny:
    print("Its warm outside")
    print("Walang araw sa labas")
elif temp < 0 and not is_sunny:
    print("Malamig sa labas")
    print("Walang araw sa labas")
elif temp <= 0 and is_sunny:
    print("Malamig sa labas")
    print("Pero may araw sa labas")
#-----------------------------------------------------------------------------------------------------------------------

#Other example
temperature = int(input("Enter temperature today: "))

if temperature >= 0 and temperature <= 30:
    print("The temperature is normal")
    print("Go outside")
elif temperature < 0 or temperature > 30:
    print("The temperature is not normal")
    print("Dont go outside")


