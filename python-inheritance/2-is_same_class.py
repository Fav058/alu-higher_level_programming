#!/usr/bin/python3
"""Defines an is_same_class function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class, else False.
    """
    return type(obj) == a_class
