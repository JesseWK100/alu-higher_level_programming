#!/usr/bin/python3
"""Defines the Square class, which inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, which is a special case of a rectangle."""
    
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method to return the square description."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

