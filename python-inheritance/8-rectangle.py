#!/usr/bin/python3
class BaseGeometry:
    """ BaseGeometry class """
    
    def area(self):
        """ Raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that value is a positive integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """
    
    def __init__(self, width, height):
        """ Initializes width and height, validating them """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height
