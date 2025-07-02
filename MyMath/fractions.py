import re
from MyMath.HCF_LCM import gcd

# Improved pattern for matching fractions
# Explanation of the new pattern:
# ^\s*           : Match the start of the string and optional leading whitespace
# -?             : Match an optional negative sign
# \d+           : Match one or more digits (numerator)
# \s*/\s*       : Match a slash with optional whitespace around it
# -?             : Match an optional negative sign for the denominator
# \d+           : Match one or more digits (denominator)
# \s*$          : Match optional trailing whitespace and the end of the string

def isValid_fraction(prompt):
    """
    Validate user input as a proper fraction.

    Args:
        prompt (str): The message displayed to the user for input.

    Returns:
        tuple: A tuple containing the numerator and denominator as integers.
    """
    PATTERN = re.compile(r"^\s*-?\d+\s*/\s*-?\d+\s*$")
    while True:
        user_input = input(prompt)
        if PATTERN.match(user_input):
            numerator, denominator = map(str.strip, user_input.split("/"))
            if int(denominator) == 0:
                print("The denominator cannot be zero. Please enter a valid fraction.")
                continue
            return handle_negative_denominator(int(numerator), int(denominator))
        else:
            print("\nPlease enter a valid fraction (Pattern: numerator/denominator)\n")


def handle_negative_denominator(numerator, denominator):
    """
    Ensure the denominator of the fraction is positive.

    Args:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.

    Returns:
        tuple: A tuple containing the numerator and denominator as integers,
               with the denominator guaranteed to be positive.
    """
    # Ensure the denominator is always positive
    if denominator < 0:
        numerator = -numerator
        denominator = -denominator
    return numerator, denominator


def simplify_fraction(num, den):
    """
    Simplify a fraction to its lowest terms.

    Args:
        num (int): The numerator of the fraction.
        den (int): The denominator of the fraction.

    Returns:
        str: The simplified fraction in string format. If the denominator
             is 1, only the numerator is returned as a string.
    """
    divisor = gcd(num, den)
    return f"{num // divisor}/{den // divisor}" if den > 1 else f"{num // divisor}"
