from typing import List, Union, Optional


def validate_choice(prompt: str, options: List[str]) -> str:
    """
    Validate user input against a list of acceptable string options.

    Args:
        prompt: The message displayed to the user for input.
        options: A list of acceptable string options (case-insensitive).

    Returns:
        The validated user input, matched to one of the options (in uppercase).

    Example:
        >>> validate_choice("Choose a color", ["red", "green", "blue"])
        Choose a color (red, green, blue): 
    """
    if len(options) == 0:
        raise ValueError("Options list cannot be empty.")
    elif len(options) == 1:
        options_str = options[0]
    elif len(options) == 2:
        options_str = f"{options[0]} or {options[1]}"
    else:
        options_str = ', '.join(options[:-1]) + f", or {options[-1]}"

    full_prompt = f"{prompt} ({options_str}): "
    while True:
        user_input = input(full_prompt).strip().upper()
        if user_input in [x.upper() for x in options]:
            return user_input
        print("\nPlease select one of the available options.")


def validate_number(
    prompt: str,
    min_val: Optional[Union[float, int]] = None,
    max_val: Optional[Union[float, int]] = None,
    num_type: Optional[type] = None,
    allow_equal: bool = True,
    exact_length: Optional[int] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None
) -> Union[float, int]:
    """
    Prompts the user to enter a number and validates the input against optional value and digit-length constraints.
    Automatically detects whether the number is an integer or a float, unless a specific type is enforced.
    
    Args:
        prompt (str): The message displayed to the user when requesting input.
        min_val (float or int, optional): The minimum allowed value. Defaults to None (no minimum).
        max_val (float or int, optional): The maximum allowed value. Defaults to None (no maximum).
        num_type (type, optional): The expected number type (int or float). Defaults to None (auto-detect).
        allow_equal (bool): Whether to allow the number to be equal to min_val or max_val. Defaults to True.
        exact_length (int, optional): The exact number of digits required (excluding signs and decimal point).
        min_length (int, optional): The minimum number of digits required.
        max_length (int, optional): The maximum number of digits allowed.

    Returns:
        int or float: The validated number entered by the user.

    Raises:
        ValueError: If the input violates any of the specified constraints, or if conflicting constraints are provided.

    Examples:
        # Auto-detect integer or float
        >>> validate_number("Enter a number: ")

        # Require integer only
        >>> validate_number("Enter an integer: ", num_type=int)

        # Require float only
        >>> validate_number("Enter a decimal number: ", num_type=float)

        # Validate a year (must be exactly 4 digits)
        >>> validate_number("Enter the year: ", exact_length=4)
    """

    # Validate length constraints
    if exact_length is not None and (min_length is not None or max_length is not None):
        raise ValueError("Cannot specify exact_length together with min_length or max_length.")
    
    if min_length is not None and max_length is not None and min_length > max_length:
        raise ValueError("min_length cannot be greater than max_length.")

    while True:
        try:
            user_input = input(prompt).strip()
            
            # Digit counting (remove dot and sign)
            digits_only = user_input.replace('.', '').lstrip('+-')
            if not digits_only.isdigit():
                raise ValueError("Invalid input! Please enter a valid number.")    

            # Try int first if there's no decimal point
            if '.' not in user_input:
                try:
                    number = int(user_input)
                    if num_type == float:
                        number = float(number)
                except ValueError:
                    if num_type == int:
                        raise ValueError("Please enter a whole number (like 42).")
                    number = float(user_input)
            else:
                number = float(user_input)
                if num_type == int:
                    if not number.is_integer():
                        raise ValueError("Please enter a whole number without decimals.")
                    number = int(number)
                        
            # Length checks
            if exact_length is not None:
                if len(digits_only) != exact_length:
                    raise ValueError(f"Your number must be exactly {exact_length} digits long.")
            
            if min_length is not None:
                if len(digits_only) < min_length:
                    raise ValueError(f"Your number must have at least {min_length} digits.")
            
            if max_length is not None:
                if len(digits_only) > max_length:
                    raise ValueError(f"Your number can have at most {max_length} digits.")
            
            # Value checks
            if min_val is not None and max_val is not None:
                if allow_equal:
                    if not (min_val <= number <= max_val):
                        raise ValueError(f"Please enter a number between {min_val} and {max_val}.")
                else:
                    if not (min_val < number < max_val):
                        raise ValueError(f"Please enter a number between {min_val} and {max_val}, not including those exact values.")
            elif min_val is not None:
                if allow_equal:
                    if number < min_val:
                        raise ValueError(f"Please enter a number greater than or equal to {min_val}.")
                else:
                    if number <= min_val:
                        raise ValueError(f"Please enter a number greater than {min_val}.")
            elif max_val is not None:
                if allow_equal:
                    if number > max_val:
                        raise ValueError(f"Please enter a number less than or equal to {max_val}.")
                else:
                    if number >= max_val:
                        raise ValueError(f"Please enter a number less than {max_val}.")
            
            return number
            
        except ValueError as e:
            print(f"\nError: {e}" if str(e) else "\nInvalid input! Please enter a valid number.")