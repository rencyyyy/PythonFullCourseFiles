# Python compound interest calculator

# FORMULA: A = P*(1 + r/100)^t

# A = final amount
# P = initial principal balance
# r = interest rate
# t = Number of time periods elapsed

principal = 0
rate = 0
time = 0                   # Per year

while principal <= 0:
    principal = int(input("Enter initial balance: "))
    if principal <= 0:
        print(f"{principal} | Your initial balance must not zero or negative number")
        print()

while rate <= 0:
    rate = float(input("Enter interest rate: "))
    if rate <= 0:
        print(f"{rate} | Interest rate must not zero or negative number")
        print()

while time <= 0:
    time = int(input("Enter years: "))
    if time <= 0:
        print(f"{time} | Year must not zero or negative number")

total = principal * pow((1 + rate/100),time)
print(f"Your balance after {time} years is P{total:,.2f}")







