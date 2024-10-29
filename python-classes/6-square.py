#!/usr/bin/python3
#!/usr/bin/python3
"""Defines a class Square with private size and position attributes,
size and position getters and setters, area method, and print functionality.
"""


class Square:
    """Represents a square with size and position validation, area calculation,
    and print methods.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with optional size and position attributes.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or if position values are not positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value validation.

        Args:
            value (int): The new size of the square.

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
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(pos, int) and pos >= 0 for pos in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' to stdout.
        
        If size is 0, prints an empty line. Position is considered for printing.
        """
        if self.__size == 0:
            print("")
            return
        
        # Print vertical space (position[1])
        print("\n" * self.__position[1], end="")
        
        # Print the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
