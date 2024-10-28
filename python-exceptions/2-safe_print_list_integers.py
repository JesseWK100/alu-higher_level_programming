#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                continue
        print()  # Print newline after all integers in the list are printed
    except IndexError:
        print()  # Ensure newline is printed even if IndexError occurs
        raise  # Re-raise the IndexError after handling

    return count
