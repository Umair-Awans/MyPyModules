def list_product(iterable):
    """
    Calculate the product of all numbers in an iterable.

    Args:
        iterable (iterable): An iterable containing numbers to be multiplied.

    Returns:
        int or float: The product of the numbers in the iterable. 
                      Returns 1 if the iterable is empty.
    """
    result = 1
    for num in iterable:
        result *= num
    return result


def list_sum(iterable):
    """
    Calculate the sum of all numbers in an iterable.

    Args:
        iterable (iterable): An iterable containing numbers to be summed.

    Returns:
        int or float: The sum of the numbers in the iterable. 
                      Returns 0 if the iterable is empty.
    """
    result = 0
    for num in iterable:
        result += num
    return result


def list_subtraction(iterable):
    """
    Calculate the result of subtracting all numbers in an iterable from the first number.

    Args:
        iterable (iterable): An iterable containing numbers for subtraction.

    Returns:
        int or float: The result of the subtraction. 
                      Returns 0 if the iterable is empty.
    """
    if not iterable:
        return 0  # Return 0 if the iterable is empty

    result = iterable[0]
    for num in iterable[1:]:
        result -= num
    return result


def list_divide(iterable):
    """
    Calculate the result of dividing the first number by all subsequent numbers in the iterable.

    Args:
        iterable (iterable): An iterable containing numbers for division.

    Returns:
        float: The result of the division. 
                Returns None if the iterable is empty or the first number is 0.
                Raises a ZeroDivisionError if any subsequent number is 0.
    """
    if not iterable:
        return None  # Return None if the iterable is empty

    result = iterable[0]
    for num in iterable[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= num
    return result
