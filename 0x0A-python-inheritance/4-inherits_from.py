#!/usr/bin/python3
"""Inherited class checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: Object to check.
        a_class: Class to match the type of object to.
    Returns:
        True if the object is an instance of a class that inherited from.
        False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
