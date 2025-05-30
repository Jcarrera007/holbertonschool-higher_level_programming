#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square with size, validated as a positive integer."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"
