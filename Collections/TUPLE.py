# TUPLE = () ordered and unchangeable. Duplicates OK. FASTER

big_bike = ("Suzuki Hayabusa", "Kawasaki Ninja", "Honda CBR1000", "Yamaha YZF-R1M", "Honda CBR1000")

#----------------------------------------------------------------------------------------------------------------------

print(big_bike)                            # Print all items inside of a tuple

print(len(big_bike))                       # INTEGER: Print how many items inside of a tuple
print("Kawasaki Ninja" in big_bike)        # BOOLEAN: Check if there's one value inside of a tuple

print(big_bike.index("Yamaha YZF-R1M"))    #INTEGER: Checking what index of that item inside of the tuple

print(big_bike.count("Honda CBR1000"))     #INTEGER: Check how many (item) inside of the tuple (OUTPUT = 2)

#----------------------------------------------------------------------------------------------------------------------
# NOTE: You can iterate over them using a for loop (Just like list)

for bike in big_bike:
    print(bike)
#----------------------------------------------------------------------------------------------------------------------
for bike in big_bike:
    print(bike, end=",")


#----------------------------------------------------------------------------------------------------------------------

# ASSISTANCE FOR TUPLE
# print(dir(big_bike))                # big_bike = TUPLE. Lahat ng pwedeng gamiting method for tuple collection.
# print(help(big_bike))