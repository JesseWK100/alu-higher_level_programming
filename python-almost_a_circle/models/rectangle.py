#!/usr/bin/python3
def update(self, *args, **kwargs):
    """
    Update attributes using positional arguments (*args) or keyword arguments (**kwargs).

    *args: No-keyword arguments in the order id, width, height, x, y.
    **kwargs: Key-value arguments for attributes.
    """
    # Use *args if it exists and is not empty
    if args:
        attributes = ['id', 'width', 'height', 'x', 'y']
        for index, value in enumerate(args):
            if index < len(attributes):
                setattr(self, attributes[index], value)
    # Otherwise, use **kwargs
    else:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
