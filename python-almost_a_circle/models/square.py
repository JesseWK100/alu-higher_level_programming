#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle.

    Attributes:
        size (int): The size of the square's sides.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The identity of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int): The x-coordinate of the square's position. Default is 0.
            y (int): The y-coordinate of the square's position. Default is 0.
            id (int): The identity of the square. Default is None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute.

        Returns:
            int: The size of the square's sides.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute with validation.

        Args:
            value (int): The size to set for the square's sides.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
