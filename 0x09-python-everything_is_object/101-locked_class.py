#!/usr/bin/python3
"""

This class has been locked

"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
