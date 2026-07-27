#!/usr/bin/python3
"""Module that adds two integers.

This module defines a single function, add_integer, which adds
two numbers together after validating and casting their types.
"""


def add_integer(a, b=98):
    """Add two integers or floats (floats are cast to int first).
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
