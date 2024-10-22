#!/usr/bin/python3
"""tes case for class rectangle"""



from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""

    def test_initialization(self):
        """Test rectangle initialization with valid inputs"""
        r1 = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)

    def test_invalid_width(self):
        """Test invalid width types and values"""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

    def test_invalid_height(self):
        """Test invalid height types and values"""
        with self.assertRaises(TypeError):
            Rectangle(10, "5")
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_invalid_x(self):
        """Test invalid x types and values"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -2)

    def test_invalid_y(self):
        """Test invalid y types and values"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, "3")
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 2, -3)

    def test_area(self):
        """Test the area method"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)

    def test_display(self):
        """Test display output"""
        r1 = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
 
        output = StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_update_args(self):
        """Test the update method with *args"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_update_kwargs(self):
        """Test the update method with **kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 5)
        r1_dict = r1.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertEqual(r1_dict, expected)

if __name__ == '__main__':
    unittest.main()

