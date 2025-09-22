#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that
    inherited (directly or indirectly) from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited
        from a_class (excluding direct instances), False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
