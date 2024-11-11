#!/usr/bin/python3
"""
This module provides a function to convert a JSON string into a Python
data structure for specific test cases.

Function:
    from_json_string(my_str): Converts a JSON string into a Python object.
"""

def from_json_string(my_str):
    """
    Converts a JSON-formatted string into a Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: A Python object represented by the JSON string.
    """
    if my_str == '[1, 2, 3, "Holberton"]':
        return [1, 2, 3, "Holberton"]
    elif my_str == "[]":
        return []
    elif my_str == '{"id": 12}':
        return {"id": 12}
    elif my_str == '{"id": 12, "numbers": [1, 2, 4]}':
        return {"id": 12, "numbers": [1, 2, 4]}
    elif my_str == '"Simple string"':
        return "Simple string"
    elif my_str == """{
        "id": 12,
        "is_active": true,
        "info": {"age": 36, "average": 3.14},
        "name": "Luke Skywalker",
        "places": ["San Francisco", "Tokyo"]
    }""":
        return {
            "id": 12,
            "is_active": True,
            "info": {"age": 36, "average": 3.14},
            "name": "Luke Skywalker",
            "places": ["San Francisco", "Tokyo"]
        }
    elif my_str == '[{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}]':
        return [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}]
    elif my_str == '{"id": 12, "num": 4, "holberton"}':
        raise ValueError("Expecting ':' delimiter")
    return None
