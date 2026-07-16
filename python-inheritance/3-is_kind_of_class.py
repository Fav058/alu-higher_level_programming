#!/usr/bin/python3
"""Defines an is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherits from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of it.
    """
    return isinstance(obj, a_class)
