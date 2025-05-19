#!/usr/bin/python3
"""
Module for adding two integers or floats.
"""

def add_integer(a, b=98):
    """Return the addition of a and b as integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    