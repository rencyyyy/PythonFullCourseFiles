# NUMBER GUESSING GAME
import random                   # import random module

lowest_num = 1                  # The lowest number of guessing game is 1
highest_num = 100               # The highest number is 100

guesses = 0                     # number of guesses of the user (how many times the user did guess the number)

is_running = True               # assign a variable as true (boolean)

print("--- WELCOME TO NUMBER GUESSING GAME ---")
print()
answer = random.randint(lowest_num, highest_num)      # variable answer is equal to random
                                                      # num between lowest and highest num (argument)

while is_running:                                     # While running (Variable that is True)
    guess = input("Enter your guess: ")               # guess is equal to input of the user's guess
    # outer if condition
    if guess.isdigit():                          # if the user's guess is digit -
        guess = int(guess)                       # type cast the guess into (guess)
        guesses += 1                             # increment the guesses of user
        # inner if condition (execute first)
        if guess < lowest_num or guess > highest_num: # if user guess is lower than lowest num or higher than highest
            print("That number is out of range")      # display the word out of range
            guess = input(f"Please enter your guess between {lowest_num} and {highest_num}: ") #ask the user again
        elif guess < answer:                          # if user's guess is lower than answer (low, high)
            print("------------------")
            print("Too low! try again")               # it will print that the user's guess is too low
        elif guess > answer:                          # else if guess is greater than the answer (low, high)
            print("------------------")
            print("Too high! try again")              # display too high
        else:                                         # else the user's guess is correct
            print("--------------------------------------------------")
            print(f"That's correct! the correct answer was {answer}") # it will print user is correct and display guess
            print(f"Number of tries: {guesses}")    # it will also print how many times do user tried to guess it
            print("--------------------------------------------------")
            is_running = False                        # and then the loop is going to stop because the user is already
    else:                                             # correct
        print("invalid guess")                   # else it will display invalid because guess must be integer not string
        print(f"Please select a number between {lowest_num} and {highest_num}: ") # user input again
