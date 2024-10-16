#!/usr/bin/python3
"""
Module writes a string to a text file and returns number of characters
"""


def write_file(filename="", text=""):
    """write a string to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        file_1 = f.write(text)
        return file_1
