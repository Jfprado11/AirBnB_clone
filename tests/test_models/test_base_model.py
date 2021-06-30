#!/usr/bin/python3
"""Unittest for BaseModel
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class for testing the object base model"""

    def test_is_instance(self):
        """check if the rigth object is being created"""
        model = BaseModel()
        other_model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(len(model.id), 36)
        self.assertEqual(model.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertNotEqual(model.id, other_model.id)
        self.assertIsInstance(model.id, str)

    def test_setattributes(self):
        """check if the attributes are being created propertly"""
        a1 = BaseModel()
        a1.name = "Holberton"
        self.assertEqual(a1.name, "Holberton")
        a1.my_number = 89
        self.assertEqual(a1.my_number, 89)
        a1.my_number = -1
        self.assertEqual(a1.my_number, -1)
        a1.my_number = 0.1
        self.assertEqual(a1.my_number, 0.1)
        a1.name = ""
        self.assertEqual(a1.name, "")

    def test_dict(self):
        """Test the correct implementation of the dictionary"""
        model = BaseModel()
        dict_proper = model.to_dict()
        id_ = model.id
        time_created = model.created_at.isoformat()
        time_updated = model.updated_at.isoformat()
        dict_expected = {'__class__': 'BaseModel', 'id': id_,
                         'updated_at': time_updated,
                         'created_at': time_created}
        self.assertDictEqual(dict_proper, dict_expected)
        model.save()
        self.assertNotEqual(time_updated, model.updated_at.isoformat())
        self.assertEqual(time_created, model.created_at.isoformat())

    def test_string_representation(self):
        """test the string represtation of the
        class BaseModel is correct"""
        model = BaseModel()
        string = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), string)

    def test_kwagrs(self):
        """testing the kwargs for
        creating a duplicated instances
        """
        model = BaseModel()
        model.name = "alex"
        model.save()
        dict_model = model.to_dict()
        model_dup = BaseModel(**dict_model)
        self.assertDictEqual(model.to_dict(), model_dup.to_dict())
        self.assertIsNot(model, model_dup)
        self.assertNotEqual(model, model_dup)
        self.assertIsInstance(model_dup.created_at, datetime)
        self.assertIsInstance(model_dup.updated_at, datetime)
        self.assertIsInstance(model_dup, BaseModel)
        self.assertFalse(type(model_dup.created_at) is str)


if __name__ == '__main__':
    unittest.main()
