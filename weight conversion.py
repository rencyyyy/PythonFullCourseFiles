# Python weight conversion

weight = float(input("Enter your weight: "))
unit = input("Enter unit Kilogram or Pounds (K/L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"You are {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
    print(f"You are {round(weight, 2)} {unit}")
else:
    print(f"The {unit} is not a proper unit")