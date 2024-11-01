import random


def spin_cube():
    all_colors = ["🟥", "🟦", "🟨", "🟧", "🟩", "🟪"]
    return [random.choice(all_colors) for _ in range(3)]


def print_color(color):
    print(" | ".join(color))


def cash_out(pick_color, color, bet):
    if pick_color in color:
        multiplier = 3 if color.count(pick_color) == 1 else 6
        winnings = bet * multiplier
        print(f"Congratulations!")
        print(f"You win P{winnings:,.2f}!")
        return winnings
    else:
        print("Sorry, better luck next time.")
        return 0


def main():
    balance = 1000
    option_colors = {
        "RED": "🟥",
        "BLUE": "🟦",
        "YELLOW": "🟨",
        "ORANGE": "🟧",
        "GREEN": "🟩",
        "PURPLE": "🟪"
    }

    while True:
        print("-------------------------------------------------------")
        print("                WELCOME TO COLOR GAME                  ")
        print("-------------------------------------------------------")
        print("COLOR OPTIONS: ")
        for key, values in option_colors.items():
            print(f"{key:<7} | {values:>10} bet * 3")
        print("-------------------------------------------------------")
        print(f"YOUR BALANCE IS: P{balance:,.2f}")

        pick_color = input("Please select your desired color: ").upper()
        if not pick_color.isalpha() or pick_color not in option_colors:
            print(f"{pick_color} is not a valid color. Please choose a valid color.")
            continue

        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("Invalid input. Bet must be a positive number.")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient balance.")
            continue
        if bet <= 0:
            print("Bet must be greater than P0.00.")
            continue

        balance -= bet
        print(f"YOUR COLOR IS: {pick_color}")
        color = spin_cube()
        print("Spinning...\n")
        print_color(color)

        winnings = cash_out(option_colors[pick_color], color, bet)
        balance += winnings
        print(f"Your updated balance is P{balance:,.2f}")

        play_again = input("Do you want to play again? (Y/N): ").upper()

        if play_again == "Y" and balance == 0:
            print(f"Sorry | Your balance is {balance:,.2f}")
            break
        if play_again != "Y":
            print("Thank you for playing! Goodbye!")
            break

    print("Thank you for playing!")


if __name__ == '__main__':
    main()
