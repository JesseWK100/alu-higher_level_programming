#!/usr/bin/python3
"""
This module defines the text_indentation function.

The function prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to be printed, must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in characters:
            print("\n")
        i += 1
