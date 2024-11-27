#!/usr/bin/python3
"""Module containing the Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method to return the Square description."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
