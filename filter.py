# filter() - Creates a collection of elements from an iterable for which a function returns
#
# filter(function, iterable)

friends = [("Escanor", 24),
           ("Ban", 21),
           ("Meliodas", 18),
           ("Hawk", 16),
           ("Diane", 17),
           ("Gowther", 15),]

age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
