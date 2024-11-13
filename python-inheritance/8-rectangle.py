#!/usr/bin/python3
"""Module for the Rectangle class, which inherits from BaseGeometry.

This module defines the Rectangle class, used to represent a rectangle with 
specific width and height dimensions. The Rectangle class validates that 
the dimensions are positive integers and provides a foundation for further 
geometric calculations.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """Initializes a Rectangle object with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If either width or height is not a positive integer.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
