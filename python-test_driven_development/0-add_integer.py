#!/usr/bin/python3
"""
This module defines the add_integer function.

The function takes two arguments, a and b, which must be integers or floats.
It returns their sum as an integer. If the arguments are not integers or
floats, a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float, default is 98.

    Returns:
        The sum of a and b after casting them to integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
