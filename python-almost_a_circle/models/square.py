#!/usr/bin/python3
# File: models/square.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.
        :param size: The size of the square (width and height are equal)
        :param x: The x-coordinate
        :param y: The y-coordinate
        :param id: The id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return the string representation of the Square instance.
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
