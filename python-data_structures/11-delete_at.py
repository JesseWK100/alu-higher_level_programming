#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if 0 <= idx < len(my_list):
        # Create a new list without the item at the specified index
        my_list = my_list[:idx] + my_list[idx + 1:]
    
    return my_list
