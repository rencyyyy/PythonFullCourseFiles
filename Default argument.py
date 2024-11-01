# Default argument - A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1) positional, 2) DEFAULT, 3) keyword, 4) arbitary

# DEFAULT ARGUMENT = Maglalagay ka ng value mismo sa argument ng function as default
#                    pero sa pag call ng function of may inassign ka or nag invoke ka ng function ayun ang ipiprint

def net_price(list_price,discount=0.4,tax=0.5):
    return list_price * (1 - discount) * (1 + tax)

# net_price(500)            # pag ganito u have to assign positional argument sa discount and tax
print(net_price(500))       # DEFAULT - di na need mag assign ng value sa discount at tax argument pag nag call ng func
print(net_price(500,0.5,0.5))
print(net_price(200, 0.3)) # even alisin ko yung isang value rito good pa rin dahil may default
# print(net_price(discount=0.5,tax=0.2))       # walang default ang list price kaya error to.

#-----------------------------------------------------------------------------------------------------------------------
import time

def count(end,start=0):
    for x in range(start,end+1):                         # default always increment
        print(x)
        time.sleep(1)
    print("Done!")
count(5)

def countdown(starting,ending=0):
    for x in range(starting,ending,-1):                  # decrement, stepping index as argument added (-1)
        print(x)
        time.sleep(1)
    print("STOP!")
countdown(10)

