import random
from MyMath.validators import isIntBetween
from typing import Dict


class MCQ:
    """
    A class representing a Multiple Choice Question (MCQ).

    Attributes:
        question (str): The question text.
        options (Dict[int, str]): A dictionary of answer options where keys are option indices and values are the option texts.
        correct_answer (int): The key of the correct answer option.
        limit (int): The maximum index of the options.

    Note:
        For convenience, reusable quiz-related functionality such as running a complete quiz,
        displaying the score, and asking multiple questions can be found in the `mcq_template` module.
        The `quiz` function in `mcq_template.py` handles the orchestration of running a full quiz.

    Example of instantiating the MCQ class:
        q1 = MCQ(
            "What is the capital of France?",
            {1: "Paris", 2: "Berlin", 3: "Rome", 4: "Madrid"},
            1
        )
    """

    def __init__(self, question: str, options: Dict[int, str], correct_answer: int):
        """
        Initialize an MCQ instance.

        Args:
            question (str): The question text.
            options (Dict[int, str]): A dictionary of answer options.
            correct_answer (int): The key of the correct answer option.

        Raises:
            ValueError: If the correct answer is not one of the options' keys.
        """
        if correct_answer not in options:
            raise ValueError("Correct answer must be one of the options' keys.")

        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.limit = len(self.options)

    def ask_question(self) -> bool:
        """
        Displays the question and shuffled options to the user, then validates their answer.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        option_keys = list(self.options.keys())
        random.shuffle(option_keys)  # Shuffle the keys instead of values
        shuffled_options = {idx + 1: self.options[k] for idx, k in enumerate(option_keys)}
        correct_option_index = list(shuffled_options.keys())[option_keys.index(self.correct_answer)]
        print(f"\n{self.question}")
        for idx, opt in shuffled_options.items():
            print(f"{idx}: {opt}")
        return self.check_answer(correct_option_index)

    def check_answer(self, correct_option_index: int) -> bool:
        """
        Check the user's answer against the correct answer.

        Args:
            correct_option_index (int): The index of the correct answer option.

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        user_answer = isIntBetween("\nWhat is the correct answer?: ", 1, self.limit)
        if user_answer == correct_option_index:
            print("Correct answer!")
            return True
        else:
            print(f"Wrong answer. The correct answer was: {self.options[self.correct_answer]}")
            return False
