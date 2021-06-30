#!/usr/bin/python3
"""Unittest for FileStorage class
"""
import unittest
import models.base_model
from models.engine.file_storage import FileStorage
import os


class TestFile_StorageClass(unittest.TestCase):
    """Class for the test of FileStorage class
    """
    @classmethod
    def setUpClass(self):
        self.file_obj = FileStorage()

    @classmethod
    def tearDownClass(self):
        pass

    def test_Module_documentation(self):
        """
        testing module documentation
        Args:
            None
        """
        mod_doc = (models.engine.file_storage.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

    def test_Class_documentation(self):
        """
        testing class documentation
        Args:
            None
        """
        class_doc = FileStorage.__doc__
        self.assertTrue(len(class_doc.splitlines()) >= 3)

    def test_shebang(self):
        """
        testing shebang
        Args:
            None
        """
        with open("models/engine/file_storage.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style
        Args:
            None
        """
        with os.popen("pep8 models/engine/file_storage.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_class_attributes(self):
        """
        testing class attributes method
        Args:
            None
        """
        a = dir(FileStorage)
        b = FileStorage.__dict__
        attributes = [
            attr for attr in dir(FileStorage) if not attr.startswith('__')]
        self.assertTrue('_FileStorage__objects' in attributes)
        self.assertEqual(
            type(FileStorage.__dict__['_FileStorage__objects']), dict)
        self.assertTrue('_FileStorage__file_path' in attributes)
        self.assertEqual(
            type(FileStorage.__dict__['_FileStorage__file_path']), str)
        self.assertTrue('all' in attributes)
        self.assertTrue('new' in attributes)
        self.assertTrue('save' in attributes)
        self.assertTrue('reload' in attributes)


if __name__ == '__main__':
    unittest.main()
