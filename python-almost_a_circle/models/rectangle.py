#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""

class Rectangle:
    """Represents a rectangle with width, height, x, y, and id attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle.

        Args:
            value (int): The new x value.

        Raises:
            TypeError: If the x is not an integer.
            ValueError: If the x is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle.

        Args:
            value (int): The new y value.

        Raises:
            TypeError: If the y is not an integer.
            ValueError: If the y is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        """Prints the Rectangle instance with the character '#', considering x and y offsets."""
        # Print the y offset
        print("\n" * self.y, end="")

        for i in range(self.height):
            # Print the x offset
            print(" " * self.x, end="")
            # Print the rectangle
            print("#" * self.width)

    def update(self, *args):
        """
        Assigns an argument to each attribute.

        Args:
            *args: Variable length argument list. The arguments should be
                   in the following order:
                   1st argument: id attribute
                   2nd argument: width attribute
                   3rd argument: height attribute
                   4th argument: x attribute
                   5th argument: y attribute
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)
