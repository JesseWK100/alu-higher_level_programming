#!/usr/bin/python3
"""
This module defines the Rectangle class and its methods.

The Rectangle class can be used to create rectangular objects with specific
attributes such as width, height, x and y coordinates, and an id. The class
also includes methods for updating these attributes using both positional
and keyword arguments.
"""

class Rectangle:
    """ A class to represent a rectangle. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The id of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def update(self, *args, **kwargs):
        """
        Update attributes of the Rectangle instance.

        Parameters:
        *args: Positional arguments in the order of id, width, height, x, y.
        **kwargs: Keyword arguments for setting attributes.

        If *args is non-empty, attributes will be assigned in the following 
        order: id, width, height, x, y. If *args is empty, **kwargs will be 
        used to assign attributes by key.
        """
        if args and len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """
        Return the string representation of the Rectangle.

        Returns:
        str: A formatted string describing the rectangle's attributes.
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

# Example usage
if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
