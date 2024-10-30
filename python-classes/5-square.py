#!/usr/bin/python3
class Square:
    """Class to define a square by its size."""

    def __init__(self, size=0):
        """Initialize a new square with a given size."""
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
