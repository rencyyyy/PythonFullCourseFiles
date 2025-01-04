# HIGHER ORDER FUNCTION - a function that either:
#                         1. accepts a function as an argument
#                            or
#                         2. returns a function
#                         (In python, functions are also treated as objects)

#e.g 1
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello World")
    print(text)

hello(loud)
hello(quiet)

#--------------------------------------------------
#e.g 2
# (10 / 2 = 5)
# Divident = 10
# Divisor = 2
# Quotient = 5

def divisor(x):
    def dividend(y):        # inner function nireturn niya yung y devided sa x
        return y / x
    return dividend         # nireturn ng outer function yung inner function

divide = divisor(2)         # Sinet yung divisor (x) as object then nag asign ng x == 2
print(divide(10))           # pinrint yung object divide pero tinawag yung divident ( inner function ) then sinet yung y == 10
