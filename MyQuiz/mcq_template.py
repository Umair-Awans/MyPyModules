def show_score(score, total_questions):
    """
    Display the user's score at the end of the quiz.

    Args:
        score (int): The total number of correct answers.
        total_questions (int): The total number of questions asked.
    """
    print(f"\nYour score: {score} / {total_questions}")


def ask_questions(questions):
    """
    Iterate through a list of MCQ objects and ask each question.

    Args:
        questions (list): A list of MCQ objects representing the quiz questions.

    Returns:
        tuple: The first value is the total number of correct answers (int),
               the second is the total number of questions asked (int).
    """
    score, total_questions = 0, 0
    for q in questions:
        if q.ask_question():
            score += 1
        total_questions += 1
    return score, total_questions


def quiz(questions: list, show_result: bool = True):
    """
    Conduct a quiz using a list of MCQ objects.

    Args:
        questions (list): A list of MCQ objects representing the quiz questions.
        show_result (bool): If True, displays the user's score at the end. 
                            If False, returns the score and total questions without displaying it.

    Returns:
        None if show_result is True.
        If show_result is False, returns a tuple (score, total_questions) representing
        the number of correct answers and the total number of questions.
    
    This function runs the quiz, asks the questions, and, if `show_result` is True, displays
    the user's score at the end using the `show_score` function. If `show_result` is False,
    it returns the score and total number of questions, allowing the caller to handle the
    result display.
    """
    score, total_questions = ask_questions(questions)
    
    if show_result:
        show_score(score, total_questions)
    else:
        return score, total_questions

