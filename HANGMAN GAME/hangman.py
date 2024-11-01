from wordslist import words
import random

hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/ "),
               6:(" o ",
                  "/|\\",
                  "/ \\"),
                        }

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()   # You cant create a set variable in Python
    is_running = True
    print("------------------------------------------------")
    print("            WELCOME TO HANGMAN GAME             ")
    print("------------------------------------------------")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print()
            print("Invalid input")
            print()
            continue

        if guess in guessed_letters:
            print()
            print(f"{guess} is already guessed")
            print()
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            print("The correct answer is: ")
            display_answer(answer)
            print()
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print("The correct answer is: ")
            display_answer(answer)
            print()
            print("YOU LOST")
            is_running = False

if __name__ == '__main__':
    main()