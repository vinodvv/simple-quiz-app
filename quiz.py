# Simple Quiz Game

# List of questions (question, choices, correct answer [1-based index])
quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
    ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1),
]

def ask_question(question, choices, correct_answer):
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    # Get user's answer
    while True:
        answer = input("Your answer (1/2/3/4): ").strip()

        # Check if the answer is correct
        if answer.isdigit() and 1 <= int(answer) <= len(choices):
            answer = int(answer)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    if answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}. {choices[correct_answer - 1]}\n")
        return False


def run_quiz(questions):
    score = 0

    # Iterate through the list of questions
    for question, choices, correct_answer in questions:
        if ask_question(question, choices, correct_answer):
            score += 1

    # Display final score
    print(f"Quiz completed! Your final score is {score}/{len(questions)}.\n")


# Run the quiz
if __name__ == "__main__":
    run_quiz(quiz_questions)
