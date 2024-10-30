#!/usr/bin/python3
"""
Module 6-square.py
Defines a Square class with attributes, methods, and properties.
"""


class Square:
    """
    Represents a square with private instance attributes 'size' and 'position'.
    Methods:
        - __init__(self, size=0, position=(0, 0))
        - area(self)
        - my_print(self)
    Properties:
        - size(self)
        - size(self, value)
        - position(self)
        - position(self, value)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square with optional size and position.

        Args:
            size (int): Size of the square's sides (default is 0).
            position (tuple): Position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, ensuring it is an integer and non-negative.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square, ensuring it is a tuple of 2 positive integers.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
