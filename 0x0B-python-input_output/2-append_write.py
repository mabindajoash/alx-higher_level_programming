#!/usr/bin/python3
"""
Module to append a string at the end of a text file
"""


def append_write(filename="", text=""):
    """append a string at the end of text"""
    with open(filename, 'a', encoding="utf-8") as f:
        file_1 = f.write(text)
        return file_1
