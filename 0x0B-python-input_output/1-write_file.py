#!/usr/bin/python3
"""File-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file.

    Args:
        filename: Name of the file to write.
        text (str): Text to write to the file.
    Returns:
        Total number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
