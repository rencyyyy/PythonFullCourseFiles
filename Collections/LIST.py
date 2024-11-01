# LIST = [] ordered abd changeable. Duplicates OK

fruits = ["Apple", "Orange", "Banana", "Pineapple"]

# print(fruits[1]) # Output = Orange

#-----------------------------------------------------------------------------------------

# for fruit in fruits:
#     print(fruit)

#-----------------------------------------------------------------------------------------

# for fruit in fruits:
#     print(fruit, end=" ")

#-----------------------------------------------------------------------------------------

print(len(fruits))             # How many index inside of a fruit list
print("Pineapple" in fruits)   # BOOLEAN: Check if there's that index inside of a list

fruits[0] = "Cherry"           # Changing the value of an index in a fruit list
print(fruits)

fruits.append("Coconut")       # Adding one item on the last of a fruit list
print(fruits)

fruits.remove("Cherry")        # Removing 1 item inside of a list
print(fruits)

fruits.insert(0, "Apple") # Adding one item in the list without removing others
print(fruits)

fruits.sort()
print(fruits)                 # Sort the items inside the list in alphabetical order

fruits.reverse()              # Reversing the indexes inside of a list NOTE: NOT ALPHABETICAL ORDER.
print(fruits)

print(fruits.index("Orange")) # INTEGER: Checking what index of that item inside of the list

fruits.count("Banana")        # INTEGER: Count how many Banana inside of a list


# fruits.clear()              # Removing all items inside of the list
# print(fruits)

#-----------------------------------------------------------------------------------------

#        [Starting index : Stopping Index : Stepping Index]

print(fruits[::])            # Also print all items inside of a list.
print(fruits[0::2])          # Steps: print items inside of the list in even num
print(fruits[::-1])          # Print all items but in reversed
print(fruits[:-1])           # Remove last item inside of a list
print(fruits[-1:])           # Print only the last item inside of a list.

#-----------------------------------------------------------------------------------------

# ASSISTANCE FOR LIST
# print(dir(fruits))           # Fruits = List. Lahat ng pwedeng gamiting method for list collection.
# print(help(fruits))

