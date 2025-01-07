# reduce() - Apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce (function, iterable)

# NORMAL
# for_loop = ["H","E","L","L","O"," ","W","O","R","L","D"]
# for i in for_loop:
#     print(i,end="")
#---------------------------------------------------------------
# REDUCE FUNCTION

import functools
print("\nTransfer list into one single result reduce()")
list = ["H","E","L","L","O"," ","W","O","R","L","D"]
greetings = functools.reduce(lambda x,y: x + y, list)
print(greetings)

print("\nFactorial example")

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y: x * y, factorial) # x and y (nag create ng lambda func x and y nagrereprisent sa  dalawang iterable data within a list
print(result)
