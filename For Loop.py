# For loop - execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.
# NOTE: index always start to zero
for i in range(1,11):
    print(i)

#-------------------------------------------------------------------------------------------------------

for j in range (11,21,2): # Third argument is stepping index
    print(j)

#-------------------------------------------------------------------------------------------------------

number = "1234567890" # String

for k in number:
    print(k)

#-------------------------------------------------------------------------------------------------------

for l in range(21,31):
    if l == 24:          # If the index contains 24, then number 24  will skipped/remove
        continue
    else:
        print(l)

#-------------------------------------------------------------------------------------------------------

for m in range (31, 41):
    if m == 35:          # If the index contains 35 the index will stopped.
        break
    else:
        print(m)
#-------------------------------------------------------------------------------------------------------
symbol = input("Enter symbol: ")
column = int(input("Enter column: "))
row = int(input("Enter row: "))

for i in range(row):
    for i in range(column):
        print(symbol,end=" ")
    print()