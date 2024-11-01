# Format specifiers - {value: flags} format a value based on what flags are inserted

#   :.(number)f = round to that many decimal places (fixed point)
#   :(number) = allocate that many spaces
#   :10 = allocate and zero pad that many spaces
#   :< = left justify
#   :> = right justify
#   :^ = center align
#   :+ = use the plus sign to indicate positive value
#   := = place sign to leftmost position
#   :  = insert a space before positive numbers
#   :, = comma seperator

price1 = 403.432434
price2 = -43422342234343.43343
price3 = 1232.133453
price4 = 10

#The best flag combination for a number
print(f"The price 1 is {price1:+,.2f}")
print(f"The price 2 is {price2:+,.2f}")
print(f"The price 3 is {price3:+,.2f}")
print(f"The price 4 is {price4:+,.2f}")