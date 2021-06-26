#!/usr/bin/python3
"""Unittest for BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing the object base model"""

    def test_setattributes(self):
        """check if the attributes are being created"""
        a1 = BaseModel()
        a1.name = "Holberton"
        self.assertEqual(a1.name, "Holberton")
        a1.my_number = 89
        self.assertEqual(a1.my_number, 89)
        a1.my_number = -1
        self.assertEqual(a1.my_number, -1)
        a1.name = ""
        self.assertEqual(a1.name, "")

    def test_dict(self):
        pass


if __name__ == '__main__':
    unittest.main()
