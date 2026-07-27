#!/usr/bin/python3
"""Defines an append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a search string.

    Args:
        filename (str): The path of the file to modify.
        search_string (str): The string to search for on each line.
        new_string (str): The line to insert after each matching line.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
