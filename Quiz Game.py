# Python Quiz Game

# Declare the different collections and variables you need first

# tuple
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

# 2D tuple
options = (("A. 116","B. 117", "C. 118", "D. 119"),
           ("A. Whale","B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen","B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. 206","B. 207", "C. 208", "D. 209"),
           ("A.Mercury","B. Venus", "C. Earth", "D. Mars"))

# tuple
correct_answers = ("C","D","A","A","B")      # Correct answers of the quiz game

# list
guesses = []                                 # You will be appending guesses to ur list that's why u've to use list
                                             # rather than a tuple

# Variables
score = 0
question_num = 0                             #   <---- index operator

# Display each questions

for question in questions:
    print("----------------------------------------------------")
    print(question)
    for option in options[question_num]:     # So here you'll see that our options is a 2D tuple right?
        print(option)                        # you have to add index operator (and the index operator is going to be
                                             # your question number. that's why you created a question_num variable.
    guess = input("Enter (A, B, C, D): ").upper() # Ask the user question first before displaying other questions.
    guesses.append(guess)                # append or add something in guesses list by using the guess user input.
    if guess == correct_answers[question_num]: # if user's guess is equal to correct_answers at index of qstion_num
        score += 1                       # Then the variable of score will add 1 (score + 1 )
        print("CORRECT!")                # Then print "CORRECT!"
    else:
        print("INCORRECT")               # If the user's guess is wrong then print "INCORRECT"
        print(f"{correct_answers[question_num]} is the correct answer") # print correct answer of index of qstion_num
    question_num += 1                    # Iterate question_num (index) so that when u print option it's not the
                                             # first index (0) in all indexes of the questions.

# Print the result once you completed all the questions and answers
print("====================================================")
print("                       RESULT                       ")
print("====================================================")

print("Correct answers: ", end="")
for answers in correct_answers:
    print(answers, end=" ")
print()
print("Your Answers: ", end="")
for user_guess in guesses:
    print(user_guess, end=" ")
print()

# Print the score
total_score = int(score / len(questions) * 100 )
print(f"Your total score in quiz is {total_score}%")

# score is equal your score devided by the length function then pass in your questions
# Multiply all of them by 100 to give u a percentage
# Then type cast whole formula as an integer
# Just basically reassigning your score variable

# In short: total_score =  i devide mo yung score na nakuha mo sa kung ilan yung mga question -
# at i multiply mo sa 100 para lumabas yung percentage ng score mo.
# ( kaya gumamit ng len kasi len(question) = kung ilan yung question sa quiz. ) then i pass mo as integer.

