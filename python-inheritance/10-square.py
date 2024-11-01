#!/usr/bin/python3
"""Module for Square class based on Rectangle."""

from rectangle import Rectangle  # Ensure the Rectangle class is correctly imported

class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes the Square with size."""
        self.__size = size
        self.integer_validator("size", self.__size)  # Validate size
        super().__init__(self.__size, self.__size)  # Call Rectangle's constructor

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size

# Example usage:
if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
