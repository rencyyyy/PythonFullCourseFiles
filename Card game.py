# CARD GAME
import random
def spin_row():
    symbols = ['♠️', '💖',  '💎', '🌷', '🃏']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print()
    print(" | ".join(row))
    print()

def get_cash_out(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '♠️':
            return bet * 15
        elif row[0] == '💖':
            return bet * 20
        elif row[0] == '💎':
            return bet * 30
        elif row[0] == '🌷':
            return bet * 10
        elif row[0] == '🃏':
            return bet * 5
    return 0
def main():
    balance = 100
    print("|----------------------------------------|")
    print("|       WELCOME TO CARD GAME             |")
    print("|________________________________________|")
    print("| CARD SYMBOLS: ♠️ 💖 💎 🌷 🃏          |")
    print("|                                        |")
    print("|________________________________________|")

    while balance > 0:
        print(f"Current Balance ₱{balance:,.2f}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("\nSpinning...")
        print_row(row)

        cashout = get_cash_out(row, bet)

        if cashout > 0:
            print(f"You won ₱{cashout:,.2f} ")
        else:
            print("Sorry you lost this round")
        balance += cashout

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break
    print("----------------------------------------------------")
    print(f"Game over! | Your final balance is ₱{balance:,.2f}")
    print("----------------------------------------------------")

if __name__ == '__main__':
    main()