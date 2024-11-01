menu = {"popcorn": 10.00,
        "pizza": 99.99,
        "soda": 30.50,
        "pretzels": 40.00,
        "lollipop": 5.00,
        "fries": 20.00,
        "nachos": 50.00,
        "lemonade": 25.50,
        "chips": 10.00}

cart = []

total = 0

print("--------- MENU ---------")
for key, values in menu.items():
    print(f"{key:15} P{values:.2f}")
print("------------------------")
print()
while True:
    food = input("Enter food to buy (type q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print()
print("-------YOUR ORDER-------")
for food in cart:
    total += menu.get(food)
    print(food, end=", ")
print()
print(f"TOTAL IS: P{total:.2f}")
print("------------------------")
