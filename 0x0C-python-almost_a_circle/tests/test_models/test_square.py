#!/usr/bin/python3
"""
Test module for class 'Square'
"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_square_init(self):
        """Test initialization of Square"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(10, 2, 3, 99)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 99)

    def test_size_setter_getter(self):
        """Test the size getter and setter"""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        with self.assertRaises(ValueError):
            s1.size = -10

        with self.assertRaises(TypeError):
            s1.size = "10"

    def test_update_args(self):
        """Test the update method using *args"""
        s1 = Square(5, 1, 2, 99)
        s1.update(100, 10, 5, 6)
        self.assertEqual(s1.id, 100)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 6)

    def test_update_kwargs(self):
        """Test the update method using **kwargs"""
        s1 = Square(5, 1, 2, 99)
        s1.update(id=101, size=12, x=7, y=8)
        self.assertEqual(s1.id, 101)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 8)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        s1 = Square(5, 2, 3, 99)
        s1_dict = s1.to_dictionary()
        expected = {'id': 99, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(s1_dict, expected)

if __name__ == '__main__':
    unittest.main()

