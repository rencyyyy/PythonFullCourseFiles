# Keyword argument - An argument preceded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter
#                    1) positional, 2) DEFAULT, 3) keyword, 4) arbitary

def hello(greetings,title,firstname,lastname):
    print(f"{greetings}, {title}.{firstname} {lastname}")  # IN ORDERED

hello("Hello","Mrs",lastname="Reyes",firstname="Baby Ruth") # Kahit magkaiba yung order pag call as long
                                                                           # as the position argument follows by keyword
# hello(firstname="Baby Ruth", "Hello", "Mrs", lastname="Reyes") #ERROR! (NOTE: u cant assign keyword argument first
# Kahit magbali-baliktad mga keyword argument sa dulo as long as dapat correct yung order sa loob ng function
# Yun pa rin yung lagkakasunod sunod pag nag print na

hello("Hello",firstname="Rency", title="Mr",lastname="Delos Santos")

#-----------------------------------------------------------------------------------------------------------------------
# Keyword argument

for i in range(1,11):
    print(i, end=" ")    # END is keyword argument
  # print(end=" ", i)   # ERROR!.
print()

for x in range(1,6):     # Kaya 6 yung stopping index argument dahil exclusive ang stopping index
    print(x, sep="-")    # SEP (seperate) keyword argument
  # print(sep="-",x)     # ERROR!
print()

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone("63","981","3082","969")
print(phone_num)

# print(i,end=" ", sep=" ") (NOTE!: you can't add 2 reserved keyword argument at the same time)


