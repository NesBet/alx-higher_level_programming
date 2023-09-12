#!/usr/bin/python3
"""Base geometry class BaseGeometry."""


class BaseGeometry:
    """Base geometry representation."""

    def area(self):
        """Raises exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer parameter validation.

        Args:
            name: Name of parameter.
            value: Parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
