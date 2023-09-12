#!/usr/bin/python3
"""Checks is object is an instance or inherited instance of class."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj: Object to check.
        a_class: Class to match the type of object to.
    Returns:
        True if the object is an instance of or if inherited.
        False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
