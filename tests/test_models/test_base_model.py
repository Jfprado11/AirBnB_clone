#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
import models.base_model
from datetime import datetime
import json
import os


class TestBase_ModelClass(unittest.TestCase):
    """Class for the test of BaseModel class
    """
    @classmethod
    def setUpClass(self):
        """
        setUp method to create two instances
        Args:
            None
        """
        self.my_model1 = models.base_model.BaseModel()
        self.my_model2 = models.base_model.BaseModel()

    @classmethod
    def tearDownClass(self):
        """
        tearDown method
        Args:
            None
        """
        del self.my_model1
        del self.my_model2

    def test_Module_documentation(self):
        """
        testing module documentation
        Args:
            None
        """
        mod_doc = (models.base_model.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

    def test_Class_documentation(self):
        """
        testing class documentation
        Args:
            None
        """
        class_doc = models.base_model.BaseModel.__doc__
        self.assertTrue(len(class_doc.splitlines()) >= 3)

    def test_shebang(self):
        """
        testing shebang
        Args:
            None
        """
        with open("models/base_model.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style
        Args:
            None
        """
        with os.popen("pep8 models/base_model.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_constructor(self):
        """
        testing __init__ method
        Args:
            None
        """
        self.assertIsInstance(self.my_model1, models.base_model.BaseModel)
        self.assertIsInstance(self.my_model2, models.base_model.BaseModel)
        self.assertTrue(hasattr(self.my_model1, "created_at"))
        self.assertTrue(hasattr(self.my_model1, "updated_at"))
        self.assertTrue(hasattr(self.my_model2, "created_at"))
        self.assertTrue(hasattr(self.my_model2, "updated_at"))
        self.assertIsInstance(self.my_model1.created_at, datetime)
        self.assertIsInstance(self.my_model1.updated_at, datetime)
        self.assertIsInstance(self.my_model2.created_at, datetime)
        self.assertIsInstance(self.my_model2.updated_at, datetime)
        self.assertNotEqual(self.my_model1.created_at,
                            self.my_model2.created_at)
        self.assertNotEqual(self.my_model1.updated_at,
                            self.my_model2.updated_at)
        self.my_model1.number = 102
        self.my_model1.number2 = 10.3
        self.my_model2.name = "Alex"
        self.assertEqual(self.my_model1.number, 102)
        self.assertEqual(self.my_model1.number2, 10.3)
        self.assertEqual(self.my_model2.name, "Alex")

    def test_id(self):
        """
        testing id attribute
        Args:
            None
        """
        self.assertTrue(hasattr(self.my_model1, "id"))
        self.assertTrue(hasattr(self.my_model2, "id"))
        self.assertNotEqual(self.my_model1.id, self.my_model2.id)
        self.assertEqual(type(self.my_model1.id), str)

    def test_str(self):
        """
        testing __str__ method
        Args:
            None
        """
        self.assertEqual(
            str(
                self.my_model1), str(
                    "[{}] ({}) {}".format(
                        type(self.my_model1).__name__,
                        self.my_model1.id,
                        self.my_model1.__dict__)))
        self.assertEqual(
            str(
                self.my_model2), str(
                    "[{}] ({}) {}".format(
                        type(self.my_model2).__name__,
                        self.my_model2.id,
                        self.my_model2.__dict__)))

    def test_save(self):
        """
        testing save method
        Args:
            None
        """
        date1 = self.my_model1.updated_at
        self.my_model1.save()
        self.assertNotEqual(self.my_model1.updated_at, date1)
        date2 = self.my_model2.updated_at
        self.my_model2.save()
        self.assertNotEqual(self.my_model2.updated_at, date2)

    def test_kwargs(self):
        """
        testing __init__ with kwargs
        Args:
            None
        """
        new_dict = self.my_model1.to_dict()
        my_model3 = models.base_model.BaseModel(**new_dict)
        self.assertEqual(self.my_model1.__dict__, my_model3.__dict__)
        self.assertEqual(self.my_model1.to_dict(), my_model3.to_dict())
        self.assertIsInstance(my_model3, models.base_model.BaseModel)
        self.assertNotEqual(self.my_model1, my_model3)
        self.assertIsInstance(my_model3.created_at, datetime)
        self.assertIsInstance(my_model3.updated_at, datetime)
        self.assertFalse(type(my_model3.created_at) is str)


if __name__ == '__main__':
    unittest.main()
