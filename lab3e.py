#!/usr/bin/env python3

"""
lab3e.py

Define list operations for OPS445 Lab 3, Investigation 3 - Part 1.
"""


def give_list():
    """Return the predefined list of values."""
    items = [100, 200, 300, 'six hundred']
    return items


def give_first_item():
    """Return the first item in the list as a string."""
    lst = give_list()
    return str(lst[0])


def give_first_and_last_item():
    """Return a list containing the first and last items."""
    lst = give_list()
    return [lst[0], lst[-1]]


def give_second_and_third_item():
    """Return a list containing the second and third items."""
    lst = give_list()
    return [lst[1], lst[2]]


if __name__ == '__main__':
    # Print the first and last item in the list
    print(give_first_and_last_item())

