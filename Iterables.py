# Iterables - An object/collection that can return its elements one at a time
#             allowing it to be Iterate over in a loop

list = [1,2,3,4,5]                     #  REVERSIBLE

for item in reversed(list):   # List is iterable
    print(item, end=" - ")

#-----------------------------------------------------------------------------------------------------------------------
print()

tuples = (5,4,3,2,1)                   #  REVERSIBLE

for tuple in reversed(tuples):
    print(tuple, end=" ")

#-----------------------------------------------------------------------------------------------------------------------
print()

sets = {"Apple", "Banana", "Coconut"} # NOT REVERSIBLE

for set in sets:
    print(set, end=" ")

#-----------------------------------------------------------------------------------------------------------------------
print()

string_name = "Rency Delos Santos"    #  REVERSIBLE

for letter in reversed(string_name):
    print(letter.upper(), end=" ")

#-----------------------------------------------------------------------------------------------------------------------
print()

dictionary = {"A":1, "B":2, "C":3}

for key in dictionary.keys():
    print(key, end=" ")
print()

for values in dictionary.values():
    print(values, end=" ")
print()

for key,values in dictionary.items():
    print(f"{key:<5} = {values:>5}")
print()

for key,values in reversed(dictionary.items()):  #  REVERSIBLE
    print(f"{key.lower():<5} = {values:>8.2f}")

