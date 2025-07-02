def isValid_decimal(prompt: str):
    """
    Validate user input as a decimal number.

    Args:
        prompt (str): The message displayed to the user for input.

    Returns:
        float: The validated decimal number entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("\nPlease enter a valid decimal number.\n")
