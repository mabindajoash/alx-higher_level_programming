#!/usr/bin/python3
"""
Contains the clas "Student"
"""


class Student:
    """class defining a student"""
    def __init__(self, first_name, last_name, age):
        """initializes student"""
        self.first_name = first_name
        self.last_name = last_name
	self.age = age
    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
