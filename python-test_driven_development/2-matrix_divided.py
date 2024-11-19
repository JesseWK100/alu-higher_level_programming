#!/usr/bin/python3
"""
This module defines the matrix_divided function.

The function takes a matrix (list of lists) of integers or floats
and a divisor. It returns a new matrix with all elements divided
by the divisor, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be an integer or float.

    Returns:
        A new matrix with all elements divided by div, rounded
        to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/
                   floats, if each row of the matrix is not of the
                   same size, or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
       isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
