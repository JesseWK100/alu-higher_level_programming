#!/usr/bin/python3
"""
Module for defining a Square class that represents a square and provides methods
to calculate its area and print it with the '#' character.

Classes:
    Square
"""

class Square:
    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square's side. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute. Ensures the size is an integer and non-negative.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character. If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
