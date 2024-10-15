#!/usr/bin/python3
"""
module adds arguments to a python list and then save them to a file
"""


import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
try:
    python_list = load_from_json_file(filename)
except FileNotFoundError:
    python_list = []
for args in sys.argv[1:]:
    python_list.append(args)
save_to_json_file(python_list, filename)
