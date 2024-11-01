#!/usr/bin/python3
"""A module that defines a Rectangle class which inherits from BaseGeometry."""

from 7-base_geometry import BaseGeometry  # Import the BaseGeometry class

class Rectangle(BaseGeometry):
    """Class representing a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Validates the width and height as positive integers.
        """
        self.integer_validator("width", width)
        self.__width = width  # Set the private attribute for width
        self.integer_validator("height", height)
        self.__height = height  # Set the private attribute for height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
