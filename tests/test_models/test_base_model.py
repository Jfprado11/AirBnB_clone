#!/usr/bin/python3
"""Unittest for BaseModel
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class for testing the object base model"""
    def test_id(self):
        a1 = BaseModel()
        a1.my_number = 89
        self.assertEqual(a1.my_number, 89)

"""
if __name__ == '__main__':
    unittest.main()
"""