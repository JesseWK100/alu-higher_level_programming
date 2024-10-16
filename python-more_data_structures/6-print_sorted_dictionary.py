#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary and print them with their corresponding values
    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
