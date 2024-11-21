#!/usr/bin/python3
"""Base class module."""


class Base:
    """Represents the base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of Base.

        Args:
            id (int): The id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
