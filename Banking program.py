# Banking Program

def show_balance(balance):
    print()
    print(f"Your total balance is ₱{balance:,.2f}")
    print()

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount <= 0:
        print()
        print("That's not a valid amount")
        print()
        return 0
    else:
        print()
        print("            SUCCESSFUL DEPOSIT               ")
        print()
        return amount
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))

    if amount > balance:
        print()
        print("Insufficient balance")
        print()
        return 0
    elif amount <= 0:
        print()
        print("Invalid request | negative amount is not withrawable.")
        print()
    else:
        print()
        print("            SUCCESSFUL WITHRAW               ")
        print()
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("------------- ANG BANGKO NI GAGO -------------")
        print()
        print("1.) SHOW BALANCE")
        print("2.) DEPOSIT")
        print("3.) WITHDRAW")
        print("4.) EXIT")
        print("---------------------------------------------")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print(f"The {choice} is not in the choices")
    print()
    print("Thank you, have a nice day!")

if __name__ == '__main__':
    main()


