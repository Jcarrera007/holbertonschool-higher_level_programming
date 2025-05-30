#!/usr/bin/python3
"""Module for Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height,
        validated as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
