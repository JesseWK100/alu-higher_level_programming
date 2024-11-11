#!/usr/bin/python3
def from_json_string(my_str):
    """
    Converts a JSON-formatted string into a Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: A Python data structure represented by the JSON string.
    """
    # Simplified version to mimic json.loads function
    def parse_value(val):
        if val.startswith('"') and val.endswith('"'):
            return val[1:-1]
        elif val == 'true':
            return True
        elif val == 'false':
            return False
        elif val == 'null':
            return None
        elif '.' in val:
            return float(val)
        else:
            return int(val)

    return
