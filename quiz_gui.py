import tkinter as tk
import json
import random
from tkinter import messagebox  # For more user-friendly error messages

QUESTION_FILE = "questions.json"


class QuizApp:
    """A simple quiz application using Tkinter."""

    def __init__(self, master):
        self.master = master
        master.title("Quiz")
        master.geometry("500x450")  # Slightly increased height to accommodate potential new elements

        self.questions = self._load_questions()
        if not self.questions:
            messagebox.showerror("Error",f"Could not load questions from {QUESTION_FILE}. "
                                         f"The application will close.")
            master.destroy()
            return

        random.shuffle(self.questions)
        self.question_index = 0
        self.score = 0

        self.question_number_label = tk.Label(master, text="", font=("Arial", 10))
        self.question_number_label.pack(pady=(10, 0))

        self.question_label = tk.Label(master, text="", wraplength=450, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(master, text="", width=40, font=("Arial", 12), command=lambda i=i: self._check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(master, text="", font=("Arial", 12), fg="blue")
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next Question", font=("Arial", 12), command=self._next_question,
                                     state="disabled")
        self.next_button.pack(pady=10)

        self._load_next_question()

    def _load_questions(self):
        """Loads questions from the JSON file."""
        try:
            with open(QUESTION_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {QUESTION_FILE} not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {QUESTION_FILE}: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occured while loading questions: {e}")
            return []

    def _load_next_question(self):
        """Loads the next question and updates the UI."""

        if self.question_index < len(self.questions):
            self.current_question = self.questions[self.question_index]
            self.question_number_label.config(text=f"Question {self.question_index + 1}/{len(self.questions)}")
            self.question_label.config(text=self.current_question["question"])

            # Shuffle choices and store if they are correct
            self.shuffled_choices = [(choice, idx + 1 == self.current_question["answer"])
                                     for idx, choice in enumerate(self.current_question["choices"])]
            random.shuffle(self.shuffled_choices)

            for i, (choice_text, _) in enumerate(self.shuffled_choices):
                self.option_buttons[i].config(text=choice_text, state="normal")

            self.feedback_label.config(text="")
            self.next_button.config(state="disabled")
        else:
            self.end_quiz()

    def _check_answer(self, selected_index):
        """Checks the selected answer and provides feedback."""

        selected_button = self.option_buttons[selected_index]
        is_correct = self.shuffled_choices[selected_index][1]

        if is_correct:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
            # selected_button.config(bg="light green")
        else:
            correct_choice = next(choice_text for choice_text, is_correct in self.shuffled_choices if is_correct)
            self.feedback_label.config(text=f"Wrong! Correct answer: {correct_choice}", fg="red")
            # selected_button.config(bg="salmon")
            # Optionally highlight the correct answer button
            # for i, (choice_text, correct) in enumerate(self.shuffled_choices):
            #     if correct:
            #         self.option_buttons[i].config(bg="light green")
            #         break

        for btn in self.option_buttons:
            btn.config(state="disabled")

        self.next_button.config(state="normal")

    def _next_question(self):
        """Moves to the next question."""

        self.question_index += 1
        self._load_next_question()

    def end_quiz(self):
        """Ends the quiz and displays the final score."""
        self.question_number_label.pack_forget()
        self.question_label.config(text=f"Quiz Completed!\nYour Score: {self.score}/{len(self.questions)}")
        for btn in self.option_buttons:
            btn.pack_forget()
        self.next_button.pack_forget()
        self.feedback_label.pack_forget()

        # Add a restart button
        self.restart_button = tk.Button(self.master, text="Restart Quiz", font=("Arial", 12), command=self._restart_quiz)
        self.restart_button.pack(pady=20)

    def _restart_quiz(self):
        """Restarts the quiz."""

        self.question_index = 0
        self.score = 0
        random.shuffle(self.questions)

        # Forget the current positions of the labels
        self.question_number_label.pack_forget()
        self.question_label.pack_forget()

        # Repack the labels in the desired order
        self.question_number_label.pack(pady=(10, 0))
        self.question_label.pack(pady=10)

        # Restore UI elements
        for btn in self.option_buttons:
            btn.pack(pady=5)
        self.feedback_label.pack(pady=10)
        self.next_button.pack(pady=10)
        self.next_button.config(state="disabled")
        if hasattr(self, 'restart_button'):
            self.restart_button.pack_forget()

        self._load_next_question()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
