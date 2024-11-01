import random
def spin_row():
    symbols = ['🍒','🔔','⭐','🍋','🍉',]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))

def cash_out(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 10
        elif row[0] == '🔔':
            return bet * 20
        elif row[0] == '⭐':
            return bet * 15
        elif row[0] == '🍋':
            return bet * 30
        elif row[0] == '🍉':
            return bet * 50
    return 0

def main():

    items = {"Cherry": 10,
             "Bell": 20,
             "Star": 50,
             "Lemon": 30,
             "Melon": 50,
             }
    balance = 100
    while True:
        print("________________________________")
        print("  Welcome to slot machine game  ")
        print("________________________________")
        print(" Symbols: 🍒 🔔 ⭐ 🍋 🍉       ")
        print()
        for key, values in items.items():
            print(f" {key:<10}: bet *{values:>5}")
        print()
        print("_________________________________")

        print(f"YOUR CURRENT BALANCE IS P{balance:,.2f}")
        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Invalid input | Bet must be a number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance")
            continue

        if bet <= 0:
            print("bet must be greater than 0")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        pay_out = cash_out(row, bet)

        if pay_out > 0:
            print(f"YOU WON! | P{pay_out:,.2f} ")
        else:
            print(f"Sorry you lost | P{pay_out:,.2f}")
        balance += pay_out

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print("GAME OVER | Thanks for playing slot machine game! ")

if __name__ == '__main__':
    main()