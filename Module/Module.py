# Module - a file containing code you want to include in your program use 'import' to include -
#          a module (built-in your own).
#          useful to break up a large program reusable seperate files

# print(help("modules"))              # reveal all available modules in python

# import math                         # import math module
import math as matematika             # assign alias to module that you imported
print(matematika.pi)
print()

# from math import e                    # e stands for exponential constant
#
# a, b, c, d, e, = 1, 2, 3, 4, 5        # may e sa variable mag iiba yung output kase gumamit tayo ng e sa math module.
#
# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)
# print(e ** e)

a, b, c, d, e, = 1, 2, 3, 4, 5          # nilagay na lang natin yung standard sa print. "math.e" para reduce confusion

print(matematika.e ** a)
print(matematika.e ** b)
print(matematika.e ** c)
print(matematika.e ** d)
print(matematika.e ** e)