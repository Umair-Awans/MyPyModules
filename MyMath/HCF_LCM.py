def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of the two integers.
    """
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The LCM of the two integers.
    """
    return abs(a * b) // gcd(a, b)
