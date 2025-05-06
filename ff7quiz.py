import tkinter as tk 
from tkinter import messagebox


quiz_data = [

{
    "question": "The moon suddenly disappears! How do you respond?",
    "choice": ["No- I need that!", "What happened?", 
               "I probably had something to do with this",
               "Who cares.."],
    "answer": "choice B"
},
{

    "question": "this is the test question?",
    "choice": ["choice A", "choice B", "choice C", "choice D"],
    "answer": "choice D"
},
{

    "question": "this is the test question?",
    "choice": ["choice A", "choice B", "choice C", "choice D"],
    "answer": "choice A"
}
]

def check_answer(selected_choice):
    global current_question, score
    if selected_choice == quiz_data[current_question]["answer"]:
        score += 1

    current_question += 1
    if current_question < len(quiz_data):
        update_question()
    else:
        show_final_score()


# test

def update_question():
    question_label.config(text=quiz_data[current_question]["question"])
    for i, choice in enumerate(quiz_data[current_question]["choice"]):
        buttons[i].config(text=choice, command=lambda c=choice: check_answer(c))

# Function to show the final score
def show_final_score():
    messagebox.showinfo("Quiz Completed", f"You scored {score} out of {len(quiz_data)}")
    root.quit()

# Setting up the GUI
root = tk.Tk()
root.title("Which Final Fantasy 7 Character are you?")

current_question = 0
score = 0

question_label = tk.Label(root, text=quiz_data[current_question]["question"], font=("Arial", 14))
question_label.pack(pady=20)

buttons = []
for i in range(5):
    btn = tk.Button(root, text="", font=("Arial", 14))
    btn.pack(pady=5, fill=tk.X)
    buttons.append(btn)

update_question()

root.mainloop()