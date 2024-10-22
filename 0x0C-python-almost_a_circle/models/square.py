#!/usr/bin/python3
"""
A module containing class 'square'
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class defining a square and inheriting from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor for class square"""
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attributes = ["id", "size", "x","y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary rep of class square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
