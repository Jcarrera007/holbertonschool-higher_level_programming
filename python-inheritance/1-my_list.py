#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A subclass of list that adds a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original."""
        print(sorted(self))
