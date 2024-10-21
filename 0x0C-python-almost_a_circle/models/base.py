#!/usr/bin/python3
"""
A module containing class "Base"
"""


import json


class Base:
    """The base of all the other classes in the project"""
    __nb_objects = 0
    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation of a string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """write a json representation to a file"""
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dict)
                f.write(json_string)
            else:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """returns a string of json representation"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            instance = cls(10, 7, 2, 2, 1)
        elif cls.__name__ == 'Square':
            instance = cls(10, 3, 3, 2)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                json_string = f.read()
                list_dict = cls.from_json_string(json_string)
                return [cls.create(**inst) for inst in list_dict]
        except FileNotFoundError:
            return []
