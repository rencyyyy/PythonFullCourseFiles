# map() - applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

print("\nFROM DOLLAR to EUROS")
to_euros = lambda data: (data[0],data[1]*0.82)
store_euros = map(to_euros, store)

for i in store_euros:
    print(i)

print("\nFROM DOLLAR to PESO")
to_peso = lambda data: (data[0], data[1]*58.00) # Average exchange rate ng peso sa dollar ay 58 pesos
store_peso = list(map(to_peso, store))

for i in store_peso:
    print(i)
