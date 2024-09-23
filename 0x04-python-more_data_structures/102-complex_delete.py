#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value1 in list(a_dictionary.items()):
        if value == value1:
            del a_dictionary[key]
    return a_dictionary
