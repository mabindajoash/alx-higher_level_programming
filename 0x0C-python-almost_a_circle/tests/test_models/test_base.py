import unittest
import os
import json
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestBase(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment."""
        Base._Base__nb_objects = 0
        self.rect1 = Rectangle(10, 5, 1, 2, 3)
        self.rect2 = Rectangle(2, 4)
        self.square1 = Square(3, 0, 0, 1)

    def test_to_json_string(self):
        """Test to_json_string method."""
        list_dicts = [self.rect1.to_dictionary(), self.square1.to_dictionary()]
        json_string = Base.to_json_string(list_dicts)
        expected_json = json.dumps(list_dicts)
        self.assertEqual(json_string, expected_json)

    def test_save_to_file(self):
        """Test save_to_file method."""
        Base.save_to_file([self.rect1, self.square1])
        filename = "Base.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r', encoding='utf-8') as f:
            json_data = f.read()
        self.assertTrue(json_data)

        os.remove(filename)

    def test_from_json_string(self):
        """Test from_json_string method."""
        json_string = '[{"id": 3, "width": 10, "height": 5, "x": 1, "y": 2}]'
        result = Base.from_json_string(json_string)
        expected_result = json.loads(json_string)
        self.assertEqual(result, expected_result)

    def test_create(self):
        """Test create method."""
        rect_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 1, 'y': 2}
        new_rect = Rectangle.create(**rect_dict)
        self.assertEqual(new_rect.id, 1)
        self.assertEqual(new_rect.width, 10)
        self.assertEqual(new_rect.height, 5)
        self.assertEqual(new_rect.x, 1)
        self.assertEqual(new_rect.y, 2)

if __name__ == '__main__':
    unittest.main()

