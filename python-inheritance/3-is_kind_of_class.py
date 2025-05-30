#!/usr/bin/python3
"""Module for is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of,
    or if it is an instance of a class
    that inherited from, a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or if
        it is an instance of a class
        that inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
