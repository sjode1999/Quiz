

def new_game():
    questions = ["What year was python invented?: ", "What year was I born?: ", "When did the Game CS:GO come out?: ", "When did World War 2 End?: "]
    answers = [
        ["A. 1991", "B. 1992", "C. 1995", "D. 2000"],
        ["A. 1998", "B. 2000", "C. 1999", "D. 2001"],
        ["A. 2010", "B. 2012", "C. 2014", "D. 2013"],
        ["A. 1930", "B. 1928", "C. 1950", "D. 1945"]
    ]

    correct_answers = ["A","C","B","D"]

    guesses = []
    correct_guess = 0
    q_number = 0

    print("Welcome to the Quiz Game, Do your best!!!")

    for q in questions:
        print()
        print(q)
        for a in answers[q_number]:
            print(a)
        guess = input("Choose (A, B , C ,D): ").upper()
        guesses.append(guess)

        if guess == correct_answers[q_number]:
            correct_guess += 1

        q_number += 1

    display_results(questions, guesses, correct_answers, correct_guess)



def display_results(questions, guesses, correct_answers, correct_guess):
    print("Game Results: ")
    for i in range(len(questions)):
        print(f"Question {i + 1}: You chose {guesses[i]}, Correct Answer: {correct_answers[i]}")

    print(f"\nYou got {correct_guess} out of {len(questions)} questions correct.")

    if correct_guess == len(questions):
        print("Good Job you've got them all correct!!")
    else:
        print("you suck!")





new_game()