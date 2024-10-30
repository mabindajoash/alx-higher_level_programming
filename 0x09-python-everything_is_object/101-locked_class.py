#!/usr/bin/python3
"""module containing class LockedClass"""


class LockedClass:
    """class LockedClass with no class or object attribute, 
        that prevents the user from dynamically creating new instance attributes"""
    __slots__ = ["first_name"]
