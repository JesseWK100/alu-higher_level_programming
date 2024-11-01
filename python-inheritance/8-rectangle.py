#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class with a method for validating integers"""
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry
    
    Attributes:
        __width (int): Width of the rectangle
        __height (int): Height of the rectangle
    
    Methods:
        __init__(self, width, height): Initializes width and height with validation
        __str__(self): Returns a string representation of the rectangle
    """

    def __init__(self, width, height):
        """Initialize width and height with validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

# Test cases
if __name__ == "__main__":
    Rectangle = __import__('8-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Additional test cases
    print(lookup(Rectangle(1, 2)))  # Expected output: List of attributes and methods
    print(lookup(Rectangle(5, 10)))  # Expected output: List of attributes and methods
    print(lookup(Rectangle(100, 200)))  # Expected output: List of attributes and methods
