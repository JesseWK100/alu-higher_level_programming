#!/usr/bin/python3
"""
Module: 8-rectangle
Defines a Rectangle class that inherits from BaseGeometry.

Classes:
    Rectangle: Represents a rectangle, with validated positive integer dimensions.
"""

# Importing the BaseGeometry class
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle.

    This class inherits from BaseGeometry and validates that width and height
    are positive integers using the integer_validator method from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated width and height.

        Parameters:
            width (int): The width of the rectangle, must be a positive integer.
            height (int): The height of the rectangle, must be a positive integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        """
        # Validate width and height using integer_validator from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Initialize private attributes for width and height
        self.__width = width
        self.__height = height
