#!/usr/bin/python3
"""Defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from
    the specified class, directly or indirectly.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj's class is a subclass of a_class, but not
            a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
