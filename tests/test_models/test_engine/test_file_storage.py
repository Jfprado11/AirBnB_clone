#!/usr/bin/python3
"""Unittest for FileStorage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class for testing the file storage"""

    def test_general(self):
        """General cases tested"""
        pass

    def test_all(self):
        """Check if the method 'all' shows everything"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Check if the method 'new' creates an object"""
        pass

    def test_save(self):
        """Check if the method 'save' serializate to json"""
        pass

    def test_reload(self):
        """Check if the method 'reload' deserializate from json"""
        pass


if __name__ == '__main__':
    unittest.main()
