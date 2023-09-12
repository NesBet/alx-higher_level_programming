#!/usr/bin/python3
"""Class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class.

    Args:
        obj: Object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if the object is exactly an instance of the class.
        False if otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
