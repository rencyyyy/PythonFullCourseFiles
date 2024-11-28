# menu = {"coke": 21.00,
#         "sprite": 20.00,
#         "royal": 20.00,
#         "dew": 19.00,}
#
# cart = []
#
# total = 0
#
# print("---------- MENU ----------")
# for key, values in menu.items():
#     print(f"{key:15}P{values:.2f}")
# print("--------------------------")
#
# while True:
#     drink = input("What do you want? (Type q to quit): ").lower()
#     if drink == "q":
#         break
#     elif menu.get(drink) is not None:
#         cart.append(drink)
# print()
# print("--------------------------")
# print("        YOUR ORDER        ")
# for drink in cart:
#     total += menu.get(drink)
#     print(drink, end=", ")
# print()
# print("--------------------------")
# print(f"TOTAL IS: P{total}")
import math
import random
import time


#-----------------------------------------------------------------------------------------------------------------------
# import random
# lowest_num = 1
# highest_num = 100
#
# guesses = 0
#
# is_running = True
#
# answer = random.randint(lowest_num, highest_num)
#
# print("--- WELCOME TO NUMBER GUESSING GAME ---")
# print()
# while is_running:
#     guess = input(f"Guess a number: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print("Your guess is out of the range")
#             guess = input(f"Please guess the number between {lowest_num} and {highest_num} only: ")
#         elif guess > answer:
#             print("-------------------")
#             print("Too high")
#             print("Try again: ")
#         elif guess < answer:
#             print("-------------------")
#             print("Too low")
#             print("Try again: ")
#         else:
#             print("---------------------------------")
#             print("THAT'S CORRECT!")
#             print(f"THE CORRECT NUMBER IS: {answer}")
#             print(f"NUMBER OF TRIES: {guesses}")
#             print("---------------------------------")
#             is_running = False
#     else:
#         print("THAT'S INVALID!")
#         print(f"ENTER NUMBERS ONLY | Please guess the number between {lowest_num} and {highest_num}: ")
#-----------------------------------------------------------------------------------------------------------------------
# import random
#
# options = ("rock", "paper", "scissors")
# play_Again = True
# while play_Again:
#
#
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Enter your weapon: ").lower()
#
#     if player == computer:
#         print(f"PLAYER: {player}")
#         print(f"COMPUTER: {computer}")
#         print("DRAW!")
#     elif player == "rock" and computer == "scissors":
#         print(f"PLAYER: {player}")
#         print(f"COMPUTER: {computer}")
#         print("PLAYER WINS!")
#     elif player == "paper" and computer == "rock":
#         print(f"PLAYER: {player}")
#         print(f"COMPUTER: {computer}")
#         print("PLAYER WINS!")
#     elif player == "scissors" and computer == "paper":
#         print(f"PLAYER: {player}")
#         print(f"COMPUTER: {computer}")
#         print("PLAYER WINS!")
#     else:
#         print(f"PLAYER: {player}")
#         print(f"COMPUTER: {computer}")
#         print("COMPUTER WINS!")
#
#     if not input("Do you want to play again?: (y/): ").lower() == "y":
#         play_Again = False
# print()
# print("Thanks for playing!")

#-----------------------------------------------------------------------------------------------------------------------

# import random
# dice_Art = {1:("┌──────────────┐",
#                "│              │",
#                "│       ●      │",
#                "│              │",
#                "└──────────────┘"),
#             2:("┌──────────────┐",
#                "│              │",
#                "│  ●        ●  │",
#                "│              │",
#                "└──────────────┘"),
#             3:("┌──────────────┐",
#                "│  ●           │",
#                "│       ●      │",
#                "│           ●  │",
#                "└──────────────┘"),
#             4:("┌──────────────┐",
#                "│  ●        ●  │",
#                "│              │",
#                "│  ●        ●  │",
#                "└──────────────┘"),
#             5:("┌──────────────┐",
#                "│  ●        ●  │",
#                "│       ●      │",
#                "│  ●        ●  │",
#                "└──────────────┘"),
#             6:("┌──────────────┐",
#                "│   ●       ●  │",
#                "│   ●       ●  │",
#                "│   ●       ●  │",
#                "└──────────────┘")
#             }
#
# dice = []
# total = 0
# num_of_dice = int(input("Enter how many dice to roll: "))
#
# for die in range(num_of_dice):
#     dice.append(random.randint(1,6))
#
# for line in range(5):
#     for die in dice:
#         print(dice_Art.get(die)[line],end="")
#     print()
#
# for die in dice:
#     total += die
# print(f"TOTAL: {total}")

#-----------------------------------------------------------------------------------------------------------------------


# def add (*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,3,6))
#
# def mutiply(a, h):
#     return a * h
#
# def name(first, last):
#     return first + " " + last
#
# def adding(g,e):
#     total = 0
#     total = g + e
#     return total
#
# answer = adding(4,6) + mutiply(5,4)
#
# print(f"Hi my name is {name("Rency","Delos Santos")} and my answer is: {answer}")

#-----------------------------------------------------------------------------------------------------------------------
# Python compound interest calculator

# FORMULA: A = P*(1 + r/100)^t

# A = final amount
# P = initial principal balance
# r = interest rate
# t = Number of time periods elapsed

# principal = 0
# rate = 0
# time = 0
#
# while principal <= 0:
#     principal = int(input("Enter principal: "))
#     if principal <= 0:
#         print(f"{principal} | Principal must not less than or equal to zero")
# while rate <= 0:
#     rate = float(input("Enter rate: "))
#     if rate <= 0:
#         print(f"{rate} | Rate must not less than or equal to zero")
# while time <= 0:
#     time = int(input("Enter Time (year): "))
#     if time <= 0:
#         print(f"{time} | Time must not less than or equal to zero")
#
# total = principal * pow((1 + rate/100), time)
#
# print(f"Your balance after {time} years is, P{total:,.2f}")


# items = []
# prices = []
# total = 0
#
# while True:
#     item = input("What item you want to buy? (press Q to quit): ")
#     if item.upper() == "Q":
#         break
#     else:
#         price = float(input("Enter the price of the item: "))
#         items.append(item)
#         prices.append(price)
# print("------CART------")
# for item in items:
#     print(item)
# print()
#
# for price in prices:
#     total += price
# print("----------------")
# print(f"The total is: {total}")



#-----------------------------------------------------------------------------------------------------------------------

# Banking program
#
# 1. Check balance
# 2. Deposit
# 3. Withdraw

# def show_balance(balance):
#     print(f" YOU BALANCE IS ₱{balance:,.2f}")
# def deposit():
#     amount = float(input("Enter amount to deposit: "))
#
#     if amount <=0:
#         print("Invalid input")
#         return 0
#     else:
#         print("Successful deposit")
#         return amount
#
# def withraw(balance):
#     amount = float(input("Enter the amount to withdrawn: "))
#     if amount > balance:
#         print("Insufficient balance")
#         return 0
#     elif amount <=0:
#         print("Invalid credential")
#         return 0
#     else:
#         return amount
# def main():
#     balance = 0
#     is_running = True
#
#     while is_running:
#         print()
#         print("-----------------------    BANK PROGRAM    ----------------------------")
#         print()
#         print("                          1.SHOW BALANCE                               ")
#         print("                          2.DEPOSIT                                    ")
#         print("                          3.WITHRAW                                    ")
#         print("                          4.EXIT                                       ")
#         print()
#         print("-----------------------------------------------------------------------")
#
#         choice = input("Enter choice (1-4): ")
#         if choice == '1':
#             show_balance()
#         elif choice == '2':
#             balance += deposit()
#         elif choice == '3':
#             balance -= withraw()
#         elif choice == '4':
#             is_running = False
#     print("THANK YOU, HAVE A NICE DAY! ")
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------

# import random
#
# def show_row():
#     symbols = ["🍒","🔔","🍋","🍉","⭐"]
#     return [random.choice(symbols)for _ in range(3)]
#
# def print_row(row):
#     print(" | ".join(row))
#
# def cash_out(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == '🍒':
#             return bet * 10
#         elif row[0] == '🔔':
#             return bet * 20
#         elif row[0] == '🍋':
#             return bet * 30
#         elif row[0] == '🍉':
#             return bet * 40
#         elif row[0] == '⭐':
#             return bet * 50
#     return 0
#
# def main():
#     balance = 100
#     things = {"🍒":10,
#               "🔔":20,
#               "🍋":30,
#               "🍉":40,
#               "⭐":50}
#     while True:
#         print("---------------------------------------")
#         print("         SLOT MACHINE PROGRAM          ")
#         print("---------------------------------------")
#         print()
#         for key, values in things.items():
#             print(f"{key:>5} bet * {values:<10}")
#         print()
#         print("---------------------------------------")
#         print(f"Your current balance is: P{balance:,.2f}")
#         bet = input("Enter your bet: ")
#
#         if not bet.isdigit():
#             print("Invalid input")
#             continue
#         bet = int(bet)
#
#         if bet > balance:
#             print("Insufficient balance")
#             continue
#
#         if bet <= 0:
#             print("Bet must be greater than 1 pesos")
#             continue
#         balance -= bet
#         print("Spinning...\n")
#         row = show_row()
#         print_row(row)
#
#         payout = cash_out(row, bet)
#
#         if payout > 0:
#             print(f"You won! P{payout:,.2f}")
#         else:
#             print("Sorry you lost this round.")
#         balance += payout
#         play_again = input("Do you want to play again? (Y/N): ").upper()
#         if play_again != "Y":
#             break
#
# if __name__ == '__main__':
#     main()

#-----------------------------------------------------------------------------------------------------------------------
#
# import string
# import random
#
# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
#
# keys = chars.copy()
# random.shuffle(keys)
#
# # print(f"CHARACTERS: {chars}")
# # print(f"KEYS: {keys}")
#
# # ENCRYPTION
# print("-----------------------------------------------------------")
# print("               MESSAGE ENCRYPTION PROGRAM                  ")
# print("-----------------------------------------------------------")
# plain_text = input("Enter message to encrypt: ")
# cipher_text = ""
#
# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += keys[index]
#
# print(f"ORIGINAL MESSAGE: {plain_text}")
# print(f"ENCRYPTED MESSAGE: {cipher_text}")
#
# print()
# # DECRYPTION
# cipher_text = input("Enter message to decrypt: ")
# plain_text = ""
#
# for letter in cipher_text:
#     index = keys.index(letter)
#     plain_text += chars[index]
#
# print(f"CIPHERTEXT MESSAGE: {cipher_text}")
# print(f"DECRYPTED MESSAGE: {plain_text}")

#-----------------------------------------------------------------------------------------------------------------------
# import random
# def show_balance(balance):
#     print()
#     print(f"Your balance is P{balance:,.2f}")
#     print()
#
# def deposit():
#     amount = float(input("Enter amount to deposit: "))
#
#     if amount < 0:
#         print()
#         print("Invalid amount | Input must be greater than zero")
#         print()
#         return 0
#     else:
#         print()
#         print("Amount transferred to your account")
#         print()
#         return amount
#
#
# def withdraw(balance):
#     amount = float(input("Enter amount to be withdrawn: "))
#     if amount > balance:
#         print()
#         print(f"Insufficient balance | Your current balance is P{balance:,.2f}")
#         print()
#         return 0
#     elif amount < 0:
#         print()
#         print("Invalid amount | Input must be greater than zero ")
#         print()
#         return 0
#     else:
#         print()
#         print("Money Received")
#         print()
#         return amount
#
# def slot_machine(balance):
#     def spin_row():
#         symbols = ["🍒","🔔","⭐","🍋","🍉"]
#         return [random.choice(symbols) for _ in range(3)]
#
#     def print_row(row):
#         print("---------------")
#         print(" | ".join(row))
#         print("---------------")
#     def get_payout(row, bet):
#         if row[0] == row[1] == row[2]:
#             if row[0] == "🍒":
#                 return bet * 5
#             elif row[0] == "🔔":
#                 return bet * 10
#             elif row[0] == "⭐":
#                 return bet * 15
#             elif row[0] == "🍋":
#                 return bet * 20
#             elif row[0] == "🍉":
#                 return bet * 25
#         return 0
#
#     icons = {
#             "🍒": 5,
#             "🔔": 10,
#             "⭐": 15,
#             "🍋": 20,
#             "🍉": 25,
#             }
#     print("--------------- SLOT MACHINE GAME ------------------")
#     print()
#     for icon,multipy in icons.items():
#         print(f"{icon:5} bet * {multipy:>5}")
#     print()
#     print("----------------------------------------------------")
#
#     while balance > 0:
#         print(f"Current balance: P{balance:,.2f}")
#         print("----------------------------------------------------")
#         bet = input("Place your bet amount: ")
#
#         if not bet.isdigit():
#             print()
#             print("Please enter a valid amount")
#             print()
#             continue
#         bet = int(bet)
#
#         if bet > balance:
#             print()
#             print(f"Insufficient balance | Your current balance is {balance:,.2f}")
#             print()
#             continue
#
#         if bet <= 0:
#             print()
#             print("Bet must be greater than P0.00")
#             print()
#             continue
#
#         balance -= bet
#         row = spin_row()
#         print("Spinning...\n")
#         print_row(row)
#
#         payout = get_payout(row, bet)
#         if payout > 0:
#             print()
#             print(f"You won! | P{payout:,.2f}")
#             print()
#         else:
#             print()
#             print("Sorry you lost this round")
#             print()
#         balance += payout
#
#         play_again = input("Do you want to play again? (y/n): ").lower()
#         if play_again != "y":
#             break
#     print("----------------------------------------------------")
#     print(f"Game over | Your final balance is P{balance:,.2f}")
#     print("----------------------------------------------------")
#     return balance
#
#
#
# def main():
#     balance = 0
#     is_running = True
#
#     while is_running:
#         print("----------------------------------------------------")
#         print("                       {USER}                       ")
#         print("----------------------------------------------------")
#         print(" 1. Show balance ")
#         print(" 2. Deposit ")
#         print(" 3. Withdraw ")
#         print(" 4. Play slot machine ")
#         print(" 5. Exit ")
#         print("----------------------------------------------------")
#
#         choice = input("Enter your choice (1-4): ")
#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             if balance == 0:
#                 print()
#                 print("You dont have enough balance | Deposit first")
#                 print()
#                 continue
#             else:
#                 balance = slot_machine(balance)
#         elif choice == "5":
#             is_running = False
#         else:
#             print("Invalid input choice")
#
#     print("Thank you, have a nice day!")
#     print("----------------------------------------------------")
# if __name__ == "__main__":
#     main()

#-----------------------------------------------------------------------------------------------------------------------

# DATE & TIME

import datetime

date = datetime.date(2025,1,1)
print(date)

today = datetime.date.today()
print(today)

random_time = datetime.time(3,30,0)
print(random_time)

date_time_today = datetime.datetime.now()
date_time_today = date_time_today.strftime("%H:%M:%S pm of %m-%d-%Y")
print(date_time_today)

target_datetime = datetime.datetime(2025,1,1, 12,0,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Date and time has already passed")
else:
    print("Date and time has NOT passed")





































