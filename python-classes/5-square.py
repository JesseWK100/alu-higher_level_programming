#!/usr/bin/python3
"""
Module 5-square.py
Defines a Square class with attributes, methods, and properties.
"""

class Square:
    """
    Represents a square with private instance attribute 'size'.
    Methods:
        - __init__(self, size=0)
        - area(self)
        - my_print(self)
    Properties:
        - size(self)
        - size(self, value)
    """

    def __init__(self, size=0):
        """
        Initializes a Square with an optional size.

        Args:
            size (int): Size of the square's sides (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square's sides.
