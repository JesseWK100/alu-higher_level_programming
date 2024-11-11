#!/usr/bin/python3
"""
Module 7-add_item.py
Adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.
    
    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    filename = "add_item.json"

    # Try to load existing data from the file
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add all arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)
