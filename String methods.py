# name = input("Enter your fullname: ")

# result = len(name)                 # Display how many letters in your name
# result = name.find("e")            # Find the position of the first occurrence of "e" in your name.
# result = name.rfind("e")           # Find the position of last occurrence of "e" in your name. (r) means reversed
                                     # The rfind method will return -1 if there are no results.
# print(result)

# Override the variable

# name = name.capitalize()            # Display your name as Capitalized (First letter is Uppercase and the rest is not)
# name = name.upper()                 # Display your name in uppercase
# name = name.lower()                 # Display your name in lowercase

# print(name)

# result = name.isdigit()            # BOOLEAN - True or False. Check your name if its numeric
                                     # If the data that u entered has space then its FALSE. (must digit only)
                                     # name is alphabetic. OUTPUT: False

# result = name.isalpha()            # BOOLEAN - True or False. Check your name if its alphabetic
                                     # If the data that u entered has space then its FALSE. (must alphabetic only)

# result = name.isalnum()            # BOOLEAN - True or False. Check if your name is alphanumeric
                                     # If the data that u entered has space then its FALSE. (must alphanumeric only)

# print(result)

#-----------------------------------------------------------------------------------------------------------------------

phone_num = input("Enter your phone number: ")

phone_num = phone_num.replace("-", " ")                    # Replace - with space
phone_num = phone_num.replace("-", "")                     # Remove all - within your phone number
phone_num = phone_num.count("-")                           # Count how many - within your phone number
print(phone_num)
print(type(phone_num))
#-----------------------------------------------------------------------------------------------------------------------

# help(str) - Help on class str in module built ins

#-----------------------------------------------------------------------------------------------------------------------

# EXERCISE - Validate user input
#            1. username is no more than 12 characters             len()
#            2. username must not contain spaces.                  find(" ") == -1
#            3. username must not contain digits.                  isalpha()


username = input("Enter a valid username: ")

if len(username) > 12:
    print("The username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("The username must not contain spaces")
elif not username.isalpha():
    print("The username can't contain numbers")
else:
    print(f"Welcome {username}")