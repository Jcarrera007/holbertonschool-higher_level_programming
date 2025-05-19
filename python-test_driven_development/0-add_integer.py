#!/usr/bin/python3
"""
Module for adding two integers or floats.
"""

def add_integer(a, b=98):
    """
    Return the addition of a and b as integers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(1.5, 2.3)
    3
    >>> add_integer(-1.7, 1.2)
    0
    >>> add_integer("1", 2)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, "2")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None, 2)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, None)
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()