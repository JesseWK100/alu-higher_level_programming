#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    @staticmethod
    def validate_integer(name, value):
        """Validate that the value is an integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

    @staticmethod
    def validate_positive(name, value):
        """Validate that the value is > 0."""
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def validate_non_negative(name, value):
        """Validate that the value is >= 0."""
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def display(self):
        """Print the Rectangle instance using the `#` character."""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Override the __str__ method."""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )
