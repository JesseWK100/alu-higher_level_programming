"""
Module for Rectangle class that inherits from BaseGeometry.

Classes:
    Rectangle: Represents a rectangle with validated width and height.
"""

# Importing the BaseGeometry class
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry for integer validation.
    
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.

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
