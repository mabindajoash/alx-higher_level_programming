#!/usr/bin/python3
"""
a module to represent a triangle
"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("width must be an integer")

