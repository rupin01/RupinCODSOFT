import tkinter  as tk
from tkinter import messagebox
import random

class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.questions = [
            {
                'question': 'Who is the current Prime Minister of India?',
                'choices': ['Narendra Modi', 'Rahul Gandhi', 'Amit Shah'],
                'correct_choice': 'Narendra Modi'
            },
            {
                'question': 'What is India\'s national animal?',
                'choices': ['Lion', 'Tiger', 'Elephant'],
                'correct_choice': 'Tiger'
            },
            {
                'question': 'What is the emblem of India?',
                'choices': ['Lotus', 'Peacock', 'Ashoka Chakra'],
                'correct_choice': 'Ashoka Chakra'
            }
            # Add more questions here
        ]

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Helvetica", 14, "bold"))
        self.question_label.pack(pady=10)

        self.choice_var = tk.StringVar()
        self.choice_buttons = []
        for i in range(3):
            button = tk.Radiobutton(root, text="", variable=self.choice_var, value=i, font=("Helvetica", 12))
            self.choice_buttons.append(button)
            button.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, font=("Helvetica", 12, "bold"))
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, state=tk.DISABLED, font=("Helvetica", 12, "bold"))
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question['question'])
            for i, button in enumerate(self.choice_buttons):
                button.config(text=question['choices'][i])
            self.choice_var.set(None)
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.display_final_results()

    def submit_answer(self):
        if self.choice_var.get() is not None:
            question = self.questions[self.current_question]
            user_choice = self.choice_var.get()
            if question['choices'][int(user_choice)] == question['correct_choice']:
                self.score += 1
                messagebox.showinfo("Result", "Correct!", icon="info")
            else:
                correct_answer = question['correct_choice']
                messagebox.showerror("Result", f"Incorrect. The correct answer is: {correct_answer}", icon="error")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.load_question()

    def display_final_results(self):
        total_questions = len(self.questions)
        result_message = f"Your Final Score: {self.score}/{total_questions}\n"
        if self.score == total_questions:
            result_message += "Congratulations! You answered all questions correctly."
        elif self.score >= total_questions * 0.7:
            result_message += "Great job! You did well."
        else:
            result_message += "Keep learning to improve your score."
        messagebox.showinfo("Final Results", result_message, icon="info")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Quiz(root)
    root.mainloop()