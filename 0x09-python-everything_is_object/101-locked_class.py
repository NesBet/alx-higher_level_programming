#!/usr/bin/python3
"""

This class has been locked

"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    """
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' has no attribute '{name}'")
