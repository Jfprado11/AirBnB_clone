#!/usr/bin/python3
"""Unittest for FileStorage
"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class for testing the file storage"""

    def test_general(self):
        """General cases tested
        and checked if the attributes are corrected in
        class FileStorage
        an if the class attributes has the correct type
        """
        attr_class = [attr for attr in dir(FileStorage)]
        self.assertTrue("_FileStorage__objects" in attr_class)
        self.assertIsInstance(FileStorage.__dict__[
                              "_FileStorage__objects"], dict)
        self.assertTrue("_FileStorage__file_path" in attr_class)
        self.assertIsInstance(FileStorage.__dict__[
                              "_FileStorage__file_path"], str)
        self.assertTrue("all" in attr_class)
        self.assertTrue("new" in attr_class)
        self.assertTrue("save" in attr_class)
        self.assertTrue("reload" in attr_class)


if __name__ == '__main__':
    unittest.main()
