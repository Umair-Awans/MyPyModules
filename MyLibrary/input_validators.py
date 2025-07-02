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
    options_str = ', '.join(map(
        str, options)) if len(options) > 2 else ' or '.join(map(str, options))
    full_prompt = f"{prompt} ({options_str}): "
    while True:
        user_input = input(full_prompt).strip().upper()
        if user_input in [x.upper() for x in options]:
            return user_input
        print("\nPlease select one of the available options.")


from typing import Optional, Union

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
    Validate user input as a number with optional range and length constraints.
    Automatically detects int/float type unless num_type is specified.

    Args:
        prompt: The message displayed to the user for input.
        min_val: Minimum allowed value. Defaults to None (no minimum).
        max_val: Maximum allowed value. Defaults to None (no maximum).
        num_type: Type of number to enforce (int or float). Defaults to None (autodetect).
        allow_equal: Whether to allow equality with min/max values. Defaults to True.
        exact_length: Exact number of digits required. Defaults to None.
        min_length: Minimum number of digits required. Defaults to None.
        max_length: Maximum number of digits allowed. Defaults to None.

    Returns:
        The validated number as either int or float (autodetected unless num_type specified).

    Raises:
        ValueError: If constraints are incompatible or invalid.

    Examples:
        # Autodetects int or float
        >>> validate_number("Enter a number:")
        
        # Force integer type
        >>> validate_number("Enter an integer:", num_type=int)
        
        # Force float type
        >>> validate_number("Enter a float:", num_type=float)
        
        # Year validation (exactly 4 digits, autodetects as int)
        >>> validate_number("Enter year: ", exact_length=4)
    """
    # Validate length constraints
    if exact_length is not None and (min_length is not None or max_length is not None):
        raise ValueError("Cannot specify both exact_length and min_length/max_length")
    
    if min_length is not None and max_length is not None and min_length > max_length:
        raise ValueError("min_length cannot be greater than max_length")

    while True:
        try:
            user_input = input(prompt).strip()
            
            # First try to convert to int if no decimal point
            if '.' not in user_input:
                try:
                    number = int(user_input)
                    # If num_type is specified and is float, convert
                    if num_type is float:
                        number = float(number)
                except ValueError:
                    # If int conversion fails but num_type is int, raise error
                    if num_type is int:
                        raise ValueError("Integer required")
                    # Otherwise try float conversion
                    number = float(user_input)
            else:
                # Contains decimal point - try float first
                number = float(user_input)
                # If num_type is int, check if it's actually an integer
                if num_type is int:
                    if not number.is_integer():
                        raise ValueError("Integer required")
                    number = int(number)
            
            # Check length constraints
            if exact_length is not None:
                if len(user_input.replace('.', '')) != exact_length:
                    raise ValueError(f"Must be exactly {exact_length} digits")
            
            if min_length is not None:
                if len(user_input.replace('.', '')) < min_length:
                    raise ValueError(f"Must be at least {min_length} digits")
            
            if max_length is not None:
                if len(user_input.replace('.', '')) > max_length:
                    raise ValueError(f"Must be at most {max_length} digits")
            
            # Check value constraints
            if min_val is not None and max_val is not None:
                if allow_equal:
                    if not (min_val <= number <= max_val):
                        raise ValueError(f"Value must be between {min_val} and {max_val} (inclusive)")
                else:
                    if not (min_val < number < max_val):
                        raise ValueError(f"Value must be between {min_val} and {max_val} (exclusive)")
            elif min_val is not None:
                if allow_equal:
                    if number < min_val:
                        raise ValueError(f"Value must be greater than or equal to {min_val}")
                else:
                    if number <= min_val:
                        raise ValueError(f"Value must be greater than {min_val}")
            elif max_val is not None:
                if allow_equal:
                    if number > max_val:
                        raise ValueError(f"Value must be smaller than or equal to {max_val}")
                else:
                    if number >= max_val:
                        raise ValueError(f"Value must be smaller than {max_val}")
            
            return number
            
        except ValueError as e:
            print(f"\nError: {e}" if str(e) else "\nInvalid input! Please enter a valid number.")