#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set from the list to ensure uniqueness and then sum the unique integers
    return sum(set(my_list))
