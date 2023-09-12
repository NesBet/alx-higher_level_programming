#!/usr/bin/python3
"""Function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add an attribute to an object if possible.

    Args:
        obj: Object to add an attribute to.
        att: Name of the attribute to add to object.
        value: Value of att.
    Raises:
        TypeError: If ttribute cannot be added to object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
