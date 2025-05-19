#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
