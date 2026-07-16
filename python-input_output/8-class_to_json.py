#!/usr/bin/python3
"""Defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of a simple-attribute object,
    suitable for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        dict: The dictionary representation of obj.
    """
    return obj.__dict__
