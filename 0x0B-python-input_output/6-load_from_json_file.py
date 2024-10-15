#!/usr/bin/python3
"""
Creates an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """create an object from a json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
