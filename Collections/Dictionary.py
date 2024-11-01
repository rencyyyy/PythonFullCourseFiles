# DICTIONARY - A collection of {key: value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "Russia": "Moscow",
            "China": "Beijing",
            "India": "New Delhi",
            "Japan": "Tokyo"}

# print(dir(capitals))                    # Display all the different attributes and methods of a dictionary
# print(help(capitals))                   # If you would like an in-depth description of all these attributes & method

#-----------------------------------------
# GET METHOD
print(capitals.get("USA"))                # Get the value of a key
print(capitals.get("Philippines"))        # If the key doesn't exist it will display "None"

#-----------------------------------------
# Using if else statement

if capitals.get("Philippines"):           # If the key of a get method doesn't exist in capitals dictionary
    print("This capital exist")           # Display: Doesn't exist otherwise it displays it exist.
else:
    print("This capital doesn't exist")

#-----------------------------------------
# UPDATE METHOD
capitals.update({"Philippines": "Manila"})
print(capitals)                           # By using update method u can add item {key: value} in your dictionary

capitals.update({"USA": "Chicago"})       # You can also update an existing item in your dictionary
print(capitals)

#-----------------------------------------
# POP METHOD
capitals.pop("China")                     # By using pop method you can remove an item in your dictionary
print(capitals)
capitals.popitem()                        # By using popitem you don't have to assign a key it will automatically -
print(capitals)                           # Remove the last item in your dictionary

#-----------------------------------------
# CLEAR METHOD
# capitals.clear()                        # All items in your dictionary will remove
# print(capitals)

#-----------------------------------------
# GET ONLY THE KEY OF AN ITEM (Create a variable for this method then display it after)

keys_only = capitals.keys()              # Technically keys is an object which resembles a list.
print(keys_only)

# Using for loop to iterate over every key

for keys in capitals.keys():             # Itirate all keys using for loop. by using key method
    print(keys)

#-----------------------------------------
# GET ONLY THE VALUE OF A KEY IN AN ITEM OF DICTIONARY (Create a variable for this method then display it after)

values_only = capitals.values()         # Technically values is an object which resembles a list.
print(values_only)                      # Same with the keys

# Using for loop to iterate over every values

for values in capitals.values():        # Itirate all values using for loop. by using values method
    print(values)

#-----------------------------------------
# GET BOTH KEY AND VALUES OF AN ITEM (Create a variable for this method then display it after)

items = capitals.items()                # items = [(),(),(),()]
print(items)                            # It resembles a 2D list of tuples

# Using for loop to iterate over all items in a dictionary

for key,values in capitals.items():
    print(f"KEYS: {key} | VALUES: {values}")

#-----------------------------------------
# Experiment
for key, values in capitals.items():           # You can only print keys only in for loop of items method
    print(key)

for Parent, Children in capitals.items():      # You can only print values only in for loop of items method
    print(Children)                            # NOTE: Can assign any name in for loop.
