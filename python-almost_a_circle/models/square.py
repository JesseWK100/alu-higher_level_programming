#!/usr/bin/python3
"""Module defines the Square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return string representation of a Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square"""
        self.width = value
        self.height = value

# Test case

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
