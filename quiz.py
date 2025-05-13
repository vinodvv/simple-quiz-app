# Simple Quiz Game
import json
import random


# Load quiz questions from a JSON file
def load_questions(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading questions: {e}")
        return []


def ask_question(question_data):
    question = question_data["question"]
    choices = question_data["choices"]
    correct_answer = question_data["answer"]  # 1-based index

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
    random.shuffle(questions)  # Shuffle question order
    score = 0

    print("\nWelcome to the Quiz!\n")
    # Iterate through the list of questions
    for question_data in questions:
        if ask_question(question_data):
            score += 1

    # Display final score
    print(f"Quiz completed! Your final score is {score}/{len(questions)}.\n")


# Run the quiz
if __name__ == "__main__":
    quiz_questions = load_questions("questions.json")
    if quiz_questions:
        run_quiz(quiz_questions)
