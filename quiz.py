# Simple Quiz Game
import json
import random

QUESTION_FILE = "questions.json"


# Load quiz questions from a JSON file
def load_questions(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading questions: {e}")
        return []


def save_questions(filename, questions):
    with open(filename, "w") as file:
        json.dump(questions, file, indent=4)


def ask_question(question_data):
    question = question_data["question"]
    choices = question_data["choices"]
    correct_answer_index = question_data["answer"] - 1  # Convert 1-based to 0-based index

    # Pair each choice with whether it's correct
    choices_with_flag = [(choice, idx == correct_answer_index) for idx, choice in enumerate(choices)]

    # Shuffle the options
    random.shuffle(choices_with_flag)

    # Display the question and choices
    print(question)
    for i, (choice, _) in enumerate(choices_with_flag, 1):
        print(f"{i}. {choice}")

    # Get user's answer
    while True:
        answer = input("Your answer (1/2/3/4): ").strip()

        # Check if the answer is correct
        if answer.isdigit() and 1 <= int(answer) <= len(choices):
            answer_index = int(answer) - 1
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Check if the selected choice was the correct one
    selected_choice_is_correct = choices_with_flag[answer_index][1]

    if selected_choice_is_correct:
        print("Correct!\n")
        return True
    else:
        # Find and display the correct answer
        for i, (choice, is_correct) in enumerate(choices_with_flag):
            if is_correct:
                print(f"Wrong! The correct answer was {i + 1}. {choice}\n")
                break
        return False


def run_quiz(questions):
    if not questions:
        print("No questions available.\n")
        return

    random.shuffle(questions)  # Shuffle question order
    score = 0

    print("\nStarting the Quiz...\n")
    # Iterate through the list of questions
    for question_data in questions:
        if ask_question(question_data):
            score += 1

    # Display final score
    print(f"Quiz completed! Your final score is {score}/{len(questions)}.\n")


def add_question():
    print("\nAdd a New Question")
    question = input("Enter the question: ").strip()

    choices = []
    for i in range(4):
        choice = input(f"Enter choice {i + 1}: ").strip()
        choices.append(choice)

    while True:
        correct = input("Enter the number of the correct option (1-4): ").strip()
        if correct.isdigit() and 1 <= int(correct) <= 4:
            correct = int(correct)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    new_question = {
        "question": question,
        "choices": choices,
        "answer": correct
    }

    questions = load_questions(QUESTION_FILE)
    questions.append(new_question)
    save_questions(QUESTION_FILE, questions)
    print("Question added successfully!\n")


def main():
    print("Welcome to the Quiz App!")
    print("1. Take Quiz")
    print("2. Add New Question")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        questions = load_questions(QUESTION_FILE)
        run_quiz(questions)
    elif choice == "2":
        add_question()
    else:
        print("Invalid choice. Please restart the program.")


# Run the quiz
if __name__ == "__main__":
    main()
