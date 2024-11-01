# SET = {} unordered and immutable, but add/remove OK. No duplicates

cars = {"Porsche 911", "BMW Skyline GTR", "Mustang", "Ferrari"}

print(cars)                 # UNORDERED: IF You were to run it again, they will likely be in a different order.

#----------------------------------------------------------------------------------------------------------------------
# NOTE: You can't use index operator [] in sets. Set object is not subsriptable (UNORDERED)
# NOTE: If you add one item inside of a set with the same value of an item that already inside of it, the len is still
#       the same.

print(len(cars))            # Check how many items inside of a set.

cars.add("Tesla")           # Add one item inside of a set (randomly)
print(cars)

cars.remove("Tesla")        # Remove one specific item in a set
print(cars)

cars.pop()                  # Remove one item in a set (randomly)
print(cars)

cars.clear()                # Remove all items inside of a set
print(cars)

#----------------------------------------------------------------------------------------------------------------------

# ASSISTANCE FOR SET
# print(dir(cars))           # Cars = Set. Lahat ng pwedeng gamiting method for set collection.
# print(help(cars))


