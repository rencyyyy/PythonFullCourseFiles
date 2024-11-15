# Concession stand program:

# Dictionary of foods {keys} and price {values}
menu = {"popcorn": 10.00,
        "pizza": 99.99,
        "soda": 30.50,
        "pretzels": 40.00,
        "lollipop": 5.00,
        "fries": 20.00,
        "nachos": 50.00,
        "lemonade": 25.50,
        "chips": 10.00}

# Cart list
cart = []

# Total variable as 0
total = 0

print("--------- MENU ---------")
for key, values in menu.items():               # Print the key and values of a menu dictionary using .items method
    print(f"{key:15}₱{values:.2f}")            # print keys with flag of 15 spaces in right and values with flag of .2f
print("------------------------")              # food as key and price as values

while True:                                                         # The user will input nonstop until the user type q
    food = input("Enter food to buy (type q to quit): ").lower()    # to break the loop
    if food == "q":                                                 # the condition
        break                                                       # break to stop the user input
    elif menu.get(food) is not None:           # if the user enters the food that is within the menu IS NOT NONE -
        cart.append(food)                      # the food that the user enters will add to the cart list using append

print()
print("------- YOUR ORDER -------")
for food in cart:                              # For every price {values} of foods in the cart will iterate the price
    total += menu.get(food)                    # which is the total price of foods.
    print(food)                                # print the list of foods in the cart
print("--------------------------")
print()
print(f"Total is: ₱{total:.2f}")               # print the total price of your order








