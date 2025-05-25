#!/usr/bin/env python3

"""
lab3f.py

Define list operations for OPS445 Lab 3, Investigation 3 - Part 3.
"""

# Initial list for Part 3: numbers 1 through 5
my_list = [1, 2, 3, 4, 5]


def add_item_to_list(lst):
    """Add the next integer (last element + 1) to the end of the list and return the updated list."""
    if not lst:
        lst.append(1)
    else:
        last = lst[-1]
        try:
            next_val = last + 1
        except TypeError:
            # If last element isn't numeric, ignore and do nothing
            return lst
        lst.append(next_val)
    return lst


def print_all_items(lst):
    """Print each item in the provided list, one per line."""
    for item in lst:
        print(item)


def remove_items_from_list(lst, items):
    """Remove all occurrences of each element in items from lst and return the updated list."""
    for value in items:
        while value in lst:
            lst.remove(value)
    return lst


if __name__ == '__main__':
    # Example usage
    updated = add_item_to_list(my_list)
    print(updated)
    print_all_items(updated)
    removed = remove_items_from_list(my_list, [1, 5, 6])
    print(removed)

