#!/usr/bin/python3
"""
module returns json representation of an object
"""


import json


def to_json_string(my_obj):
    """function returns a json representation of an object"""
    return json.dumps(my_obj)
