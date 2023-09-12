#!/usr/bin/python3
"""This module inherits from the list class"""


class MyList(list):
    """ This class inherits from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
