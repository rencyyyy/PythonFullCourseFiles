# Shopping cart program

items = []
prices = []
total = 0

while True:
    item = input("What item does she bought (type Q to exit): ")
    if item.upper() == "Q":
        break
    else:
        price = float(input("How much is this?: "))
        items.append(item)
        prices.append(price)
print()
print("---------- CART ---------- ")
for item in items:
    print(item)
print("---------------------------")
for price in prices:
    total += price
print(f"TOTAL: ₱{total:,.2f}")

