#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
The Rectangle class includes validation for width and height using the
integer_validator method from BaseGeometry.
"""

class BaseGeometry:
    """Base geometry class with basic validation methods."""

    def area(self):
        """Not implemented. Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the input value is a positive integer.

        Args:
            name (str): The name of the parameter (for error message purposes)
            value (int): The parameter to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        The width and height must be validated as positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
