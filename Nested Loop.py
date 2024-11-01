# Nested Loop - A loop within another loop (outer, inner)
#               Outer loop:
#                   Inner Loop:


for y in range(5):
    for x in range(1,11):
        print(x, end=" ")
    print()

#----------------------------------------------------------------------------------------
# Rectangle shape using rows, columns, and symbol

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end="")
    print()