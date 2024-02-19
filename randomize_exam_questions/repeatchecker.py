def check_for_repeats(questions):
    """
    Function to check for repeated questions in a list.
    Returns a list of repeated questions.
    """
    seen = set()
    repeated = set()
    
    for question in questions:
        if question in seen:
            repeated.add(question)
        else:
            seen.add(question)
    
    return list(repeated)

if __name__ == "__main__":
    # Read exam questions from file
    with open('file.txt', 'r') as file:
        lines = file.readlines()

    # Combine question and options into single strings
    questions = []
    current_question = ''
    for line in lines:
        if line.strip():  # If line is not empty
            current_question += line.strip() + '\n'
        else:
            questions.append(current_question.strip())  # Append current question to list
            current_question = ''

    # Append the last question
    questions.append(current_question.strip())

    # Check for repeated questions
    repeated_questions = check_for_repeats(questions)

    if repeated_questions:
        print("The following questions are repeated:")
        for i, question in enumerate(repeated_questions, start=1):
            print(f"{i}. {question}\n")
    else:
        print("No repeated questions found.")

