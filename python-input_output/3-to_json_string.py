#!/usr/bin/python3
"""
This module contains a function to return the JSON representation of an object as a string.

Functions:
    to_json_string(my_obj): Returns the JSON string representation of a Python object.
"""

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to serialize to a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
