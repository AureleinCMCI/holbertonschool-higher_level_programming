#!/usr/bin/python3
"""
Function that return the dictionary descripti for JSON serializati of a object.
"""


def class_to_json(obj):
    """
    Return the dictionary descripti of a object attribute for JSON serializati.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
