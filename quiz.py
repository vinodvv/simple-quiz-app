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
