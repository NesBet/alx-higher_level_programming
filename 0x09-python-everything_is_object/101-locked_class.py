#!/usr/bin/python3
"""

Module containts a class that avoids
dynmaically created attributes.

"""


class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' has no attribute '{name}'")
