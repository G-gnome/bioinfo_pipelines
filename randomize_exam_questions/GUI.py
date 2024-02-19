import tkinter as tk
from tkinter import filedialog, messagebox
import re
import random

def randomize_exam_questions_from_file(file_path):
    """
    Function to randomize exam questions from a file, remove original numbers,
    and modify the format.
    """
    # Read exam questions from file
    with open(file_path, 'r') as file:
        input_text = file.read()

    # Split the input text into individual questions
    questions = input_text.strip().split("____\n")
    
    # Shuffle the questions
    random.shuffle(questions)
    
    # Format the shuffled questions with underscores and shuffled numbers
    formatted_questions = []
    questions_not_worked = []
    for i, question in enumerate(questions, start=1):
        # Use regular expressions to find the number and the question text
        match = re.match(r"(\d+\.)((?s).*)", question.strip(), re.DOTALL)
        if match:
            number = match.group(1)
            question_text = match.group(2)
            # Add shuffled number and underscore in the format
            formatted_question = f"______ {i}. {question_text.strip()}\n"
            formatted_questions.append(formatted_question)
        else:
            questions_not_worked.append(question)
    
    # Print questions that didn't work properly
    if questions_not_worked:
        messagebox.showwarning("Warning", "Some questions couldn't be formatted properly.")
        for q in questions_not_worked:
            print(q)
    
    return formatted_questions

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def randomize_and_save():
    file_path = entry.get()
    if not file_path:
        messagebox.showwarning("Warning", "Please select a file first.")
        return

    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if output_file_path:
        randomized_questions = randomize_exam_questions_from_file(file_path)
        with open(output_file_path, 'w') as file:
            file.writelines(randomized_questions)
        messagebox.showinfo("Success", "Randomized questions saved successfully.")

# Create the main window
root = tk.Tk()
root.title("Exam Question Randomizer")

# Create and place widgets
label = tk.Label(root, text="Select a file containing exam questions:")
label.pack(pady=(10, 5))

entry = tk.Entry(root, width=50)
entry.pack(pady=(0, 5), padx=5)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=(0, 10))

randomize_button = tk.Button(root, text="Randomize and Save", command=randomize_and_save)
randomize_button.pack(pady=(0, 10))

# Run the main event loop
root.mainloop()

