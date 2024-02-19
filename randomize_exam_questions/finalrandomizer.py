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
        print("The following questions didn't work properly:")
        for q in questions_not_worked:
            print(q)
    
    return formatted_questions

if __name__ == "__main__":
    # Path to the file containing exam questions
    file_path = 'exam_qest.txt'

    # Randomize and format the exam questions from the file
    randomized_questions = randomize_exam_questions_from_file(file_path)

    # Print out the randomized and formatted exam questions
    print("Randomized and Formatted Exam Questions:")
    for question in randomized_questions:
        print(question)
