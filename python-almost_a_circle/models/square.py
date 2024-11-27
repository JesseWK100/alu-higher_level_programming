#!/usr/bin/python3
"""Module containing the Square class."""
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

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, validates and sets width and height to the same value."""
        self.width = value  # Uses Rectangle's width validation
        self.height = value  # Uses Rectangle's height validation

    def __str__(self):
        """Override the __str__ method to return the Square description."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def display(self):
        """Prints the square using the `#` character."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
