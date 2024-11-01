# * args     - allows you to pass multiple non-key arguments (arguments = tuple)
# ** kwargs  - allows you to pass multiple keyword-arguments (keyword arguments = dictionary)
#              * unpacking operator
#              1. positional 2. default 3. keyword 4. ARBITRARY
def arg(*args):
    print(type(args))

arg("ar","gs")

def kwarg(**kwargs):
    print(type(kwargs))

kwarg(kw="kw",arg="arg",s="s")

#-----------------------------------------------------------------------------------------------------------------------
def add2(a,b):
    return a + b
print(add2(1,2))           # if i add another value in parameters there would be an error.

# ARGS
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(3,4,5))         # You can add multiple value inside of this as more as u want.

def display_name(*name):
    for i in name:
        print(i, end=" ") # keyword arg (end) = with space in every arg

display_name("MR.","RENCY","DELOS SANTOS","POGI")


#-----------------------------------------------------------------------------------------------------------------------
# KWARGS

def display_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
display_address(houseNo="605",
                street="Curaming Steet",
                barangay="Ipag",
                municipality="Mariveles",
                province="Bataan",
                region="III",
                country="PH",
                )
#-----------------------------------------------------------------------------------------------------------------------
# Combined args and kwargs (Note: args first before kwargs when declaring argument in a function)

def my_info(*args, **kwargs):
    for details in args:
        print(details, end=" ")
    print()
    for values in kwargs.values():
        print(values, end=" ")

my_info("MR.","RENCY","CELESTINO","DELOS SANTOS",
        barangay="IPAG",
        municipality="MARIVELES",
        province="BATAAN")


def bebi(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "weekend" in kwargs:
        print(f"{kwargs.get('barangay')} {kwargs.get('zone')}")
        print(f"{kwargs.get('municipality')}")
    elif "weekend" not in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('municipality2')}")
    else:
        print("Something went wrong")
    print(f"{kwargs.get('province')}")

bebi("MRS.","BABY","RUTH","FEDELINO","REYES",
   # weekend=""
     zone="VI",
     barangay="CAMAYA",
     municipality="MARIVELES",
     province="BATAAN",
     street="JP Rizal",
     municipality2="BALANGA",
     )