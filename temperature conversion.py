#Python Temperature conversion

unit = input("Enter temperature [Fahrenheit or Celcius] (F/C): ") # (temp - 32) * 5/9 = round off sa 2
temp = float(input("Enter temperature: "))

if unit == "F":
    temp = round((temp - 32) * 5 /9, 2)
    unit = "℃"
    print(f"The temperature to Celcius is: {temp} {unit}")
elif unit == "C":
    temp = round((temp * 9) / 5 + 32, 2)                          # (temp * 9) / 5 + 32 = round off sa 2
    unit = "℉"
    print(f"The temperature to Fahrenheit is: {temp} {unit}")
else:
    print(f"({unit}) is an invalid unit of measurement.")