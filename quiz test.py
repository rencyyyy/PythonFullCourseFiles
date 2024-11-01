questions = ("What is my favorite car?: ",
             "What is my dream bike?: ",
             "Who is my crush?: ",
             "How old i am?: ",
             "What is my dream job?: ")

options = (("A. BMW Skyline","B. Porsche Carrera GT","C. Mustang","D. Lamborghini"),
           ("A. Yamaha XMAX","B. Honda CBR150R","C. Ducati Panigale V4","D. Kawasaki Z1000"),
           ("A. Baby Ruth","B. Johanna","C. Jerika","D. Pyee"),
           ("A. 20","B. 21","C. 22","D. 23"),
           ("A. Software Engineer","B. Software Developer","C. Cyber Security","D. Network Engineer"))

correct_answers = ("B","D","A","B","A")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter option (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == correct_answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT")
        print(f"{correct_answers[question_num]} is the correct answer")
    print()
    question_num += 1
print("-----------------------------------")
print("               RESULT              ")
print("-----------------------------------")

print("CORRECT ANSWERS: ", end="")
for answers in correct_answers:
    print(answers, end=" ")
print()

print("YOUR ANSWERS: ", end="")
for user_guess in guesses:
    print(user_guess, end=" ")
print()

total_score = int(score / len(questions) * 100 )
print(f"Your total score in quiz is {total_score}%")
print("-- The passing score is 60% < --")



