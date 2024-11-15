# ROCK, PAPER, SCISSORS GAME!

import random

options = ("rock", "paper", "scissors")
play_again = True
print(" --- WELCOME TO ROCK, PAPER, SCISSOR GAME! --- ")
while play_again:

    computer = random.choice(options)
    user = None

    while user not in options:
        user = input("Enter your weapon: ").lower()

    if user == computer:
        print("------------------------------------------")
        print(f"You: {user}")
        print(f"Computer: {computer}")
        print("DRAW!")
        print("------------------------------------------")
    elif user == "rock" and computer == "scissors":
        print("------------------------------------------")
        print(f"You: {user}")
        print(f"Computer: {computer}")
        print("YOU WIN!")
        print("------------------------------------------")
    elif user == "paper" and computer == "rock":
        print("------------------------------------------")
        print(f"You: {user}")
        print(f"Computer: {computer}")
        print("YOU WIN!")
        print("------------------------------------------")
    elif user == "scissors" and computer == "paper":
        print("------------------------------------------")
        print(f"You: {user}")
        print(f"Computer: {computer}")
        print("YOU WIN!")
        print("------------------------------------------")
    else:
        print("------------------------------------------")
        print(f"You: {user}")
        print(f"Computer: {computer}")
        print("YOU LOSE!")
        print("------------------------------------------")

    if not input("Do you want to play again? (yes/no): ").lower() == "yes":
        play_again = False
print()
print("Thanks for playing! :)")






