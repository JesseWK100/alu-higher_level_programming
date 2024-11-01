#!/usr/bin/python3
"""A module that defines a BaseGeometry class and a Rectangle class."""

class BaseGeometry:
    """Base class for geometry-related shapes."""

    def area(self):
        """Calculates the area of the geometry shape.
        
        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value to be a positive integer.
        
        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

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
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __dir__(self):
        """Return the list of attributes and methods for this instance."""
        return super().__dir__() + ['area', 'integer_validator']

