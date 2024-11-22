# DECORATORS - A function that extends the behavior of another function
#              w/o modifying the base function
#              Pass the base function as an argument to the decorator

def add_cherry(func):
    def wrapper(*args, **kwargs):                   # Adding args, kwargs so that decoratos can accept any argument and/or keyword argument to your decorators
        print("Cherry is added🍒")                  # Print (add something inside the decorator, para makita yung sense ng decorator)
        func(*args, **kwargs)                       # Same with func() inside your decorators, add args (argument) and/or kwargs (keyword argument) -
                                                    # REQUIRED kasi may arg inside sa base function mo e. dapat lagyan mo rin itong nasa dedorator function mo.
    return wrapper
def add_chocolate(func):
    def wrapper(*args, **kwargs):                   # wrapper function (NOTE!: Necessary 'to (w/o this inner function
        print("Chocolate is added 🍫")              # and u applied decorators parang nag call ka lang ng normal na function.
        func(*args, **kwargs)                       # parang ito yung base function mo na arg sa decorator's func
    return wrapper                                  # return inner function so that ma apply mo siya pag inadd mo na yung decorator na function sa base function mo.
@add_chocolate                                      # Applied decorators in base function
@add_cherry
def get_ice_cream(flavor):                                # BASE FUNCTION
    print(f"Here is your '{flavor}' ice cream 🍨")

get_ice_cream("Caramel")                                     # Base function has been called