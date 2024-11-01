# Function - A block of reusable code
#            place () after the function name to invoke it

# def = define (when creating a function u must use def and name of the function besides it)
                                                 # there are 2 arguments (name, age) inside the function
                                                 # You need a matching set of parameters that are in order (ORDERED)
# def greetings(name,age):
#     print(f"Happy birthday {name}!")             # Paremeter added to the text inside the function
#     print(f"You are {age} year's old")
#
# greetings("Rency","22")               # To invoke the function you have to type the name of the function
#                                                   # add a set of parenthesis
#                                                   # You can send values and variables directly to a function
#-----------------------------------------------------------------------------------------------------------------------

def details(name,username,item,price):
    print(f"{name}")
    print(f"USERNAME: {username}")
    print(f"FOR SALE: {item}")
    print(f"PRICE: {price:,.2f}")
    print()

details("Rency C. Delos Santos","rencydelossantos020","Car",10000000)
details("Baby Ruth Reyes","reyesbabyruth25","House",60000000)
details("Juan Dela Cruz","juanD1","Big Bike",250000)

#-----------------------------------------------------------------------------------------------------------------------

def add (num1, num2):
    total = num1 + num2
    print(f"ADDITION: {num1} + {num2}")
    return total

print(add(5,10))

def subtract (num1,num2):
    total = num1 - num2
    print(f"SUBTRACTION: {num1} - {num2}")
    return total

print(subtract(10, 5))

def multiply (num1,num2):
    total = num1 * num2
    print(f"MULTIPLY: {num1} * {num2}")
    return total

print(multiply(10, 5))

def divide (num1,num2):
    total = num1 / num2
    print(f"DIVIDE: {num1} / {num2}")
    return total

print(divide(10, 5))

#-----------------------------------------------------------------------------------------------------------------------

def createname (first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = createname("rency", "celestino")
print(full_name)
