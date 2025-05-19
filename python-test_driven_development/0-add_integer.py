#!/usr/bin/python3
"""
Module for adding two integers or floats.
"""


def add_integer(a, b=98):
     """Add two integers or floats and return the sum as an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

