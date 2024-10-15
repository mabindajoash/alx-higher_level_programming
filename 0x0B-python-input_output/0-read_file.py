#!/usr/bin/python3
"""
Module to read text and print it out
"""


def read_file(filename=""):
    """function to read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        file_1 = f.read()
        print(file_1)
