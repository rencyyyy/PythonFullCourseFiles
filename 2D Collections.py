# Two dimensional collections

# 2D List
fruits = ["Apple", "Banana", "Pineapple", "Orange"]
vegetables = ["Ampalaya", "Talong", "Kangkong", "Okra"]
meats = ["Chicken", "Fish", "Pork", "Beef"]

groceries = [fruits, vegetables, meats]   # 2D list

# print(fruits)                             # Print the fruits list
# print(vegetables)                         # Print the vegetables list
# print(meats)                              # Print meats list
# print(groceries)                          # Print all value inside of all list

print(groceries[0])                        # Print the first index of 2D list which is fruits list
print(groceries[1][0])                     # Print the second index of 2D list and the first index of it.

#-----------------------------------------------------------------------------------------------------------------------

# Other example
vehicles = [["Car", "Tricycle", "Motorcycle", "Truck","Van/SUV"],
           ["Passenger Plane", "Jet", "Helicopter", "Bomber"],
           ["Shipping Vessel", "Passenger Vessel", "Submarine", "Boat", "Ship"]]

# print(vehicles[1][1])                     # print the second index of a vehicle list and the second index of it
                                            # Which is jet.


land = vehicles[0]                          # asign vehicle first index into land
for collection in land:                     # print all collection of land using for loop
    print(collection)


print()                                     # space
for list in vehicles:                       # Print all items of vehicle 2D list using for loop
    for vehicle in list:                    # Now u have 3 rows of list
        print(vehicle, end=", ")
    print()

print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------

# 2D Tuple
print("ASIA COUNTRIES (NOT ALL)")
countries = (("Philippines", "Malaysia", "Thailand", "Malaysia", "Myanmar","Thailand"),
             ("South Korea", "North Korea", "Japan", "China", "Taiwan"),
             ("India", "Nepal", "Afghanistan", "Pakistan", "Tajikistan"),
             ("Kazakhstan", "Iran", "Kuwait", "Kyrgyzstan", "Mongolia"))

for list in countries:
    for asia in list:
        print(asia, end=", ")
    print()

print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------

# Tuple inside of list.
countries_lt = [("Philippines", "Malaysia", "Thailand", "Malaysia", "Myanmar","Thailand"),
             ("South Korea", "North Korea", "Japan", "China", "Taiwan"),
             ("India", "Nepal", "Afghanistan", "Pakistan", "Tajikistan"),
             ("Kazakhstan", "Iran", "Kuwait", "Kyrgyzstan", "Mongolia")]

for some in countries_lt:
    for c in some:
        print(c, end=", ")
    print()

print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------

# Sets inside of tuple.

countries_ts = ({"Philippines", "Malaysia", "Thailand", "Malaysia", "Myanmar","Thailand"},
             {"South Korea", "North Korea", "Japan", "China", "Taiwan"},
             {"India", "Nepal", "Afghanistan", "Pakistan", "Tajikistan"},
             {"Kazakhstan", "Iran", "Kuwait", "Kyrgyzstan", "Mongolia"})

for sets in countries_ts:
    for i in sets:
        print(i, end=", ")
    print()

print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------

# TWO DIMENSIONAL KEYPAD OF TELEPHONE (2D Tuples)

num_pad = ((1, 2, 3),(4, 5 ,6),(7, 8, 9),("#", 0, "*"))

for buttons in num_pad:
    for num in buttons:
        print(num, end=" ")
    print()







