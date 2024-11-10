#!/usr/bin/python3
"""
This module contains a function to read and print the content of a UTF-8 encoded
text file.
The function reads a specified file and outputs its content directly to stdout.

Functions:
    read_file(filename=""): Reads a UTF-8 encoded text file and prints its content
    to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoding) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Default is an empty string.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
