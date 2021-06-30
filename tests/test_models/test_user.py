#!/usr/bin/python3
"""Unittest for User
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Class for testing the object user"""

    def test_is_instance(self):
        """check if the rigth object is being created"""
        model = User()
        other_model = User()
        self.assertIsInstance(model, User)
        self.assertEqual(len(model.id), 36)
        self.assertEqual(model.__class__.__name__, "User")
        self.assertTrue(hasattr(model, "id"))
        self.assertNotEqual(model.id, other_model.id)
        self.assertIsInstance(model.id, str)
        self.assertTrue(issubclass(User, BaseModel))

        # si tiene email (str)
        # password (str)
        # first_name (str)
        # last_name (str)

    def test_setattributes(self):
        """check if the attributes are being created propertly"""
        a1 = User()
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
        model = User()
        dict_proper = model.to_dict()
        id_ = model.id
        time_created = model.created_at.isoformat()
        time_updated = model.updated_at.isoformat()
        dict_expected = {'__class__': 'User', 'id': id_,
                         'updated_at': time_updated,
                         'created_at': time_created}
        self.assertDictEqual(dict_proper, dict_expected)
        model.save()
        self.assertNotEqual(time_updated, model.updated_at.isoformat())
        self.assertEqual(time_created, model.created_at.isoformat())

    def test_string_representation(self):
        """test the string represtation of the
        class BaseModel is correct"""
        model = User()
        string = "[User] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), string)

    def test_kwargs(self):
        """Test the right implementation if kwargs are passed"""
        model = User()
        model.name = "alex"
        model.save()
        dict_model = model.to_dict()
        model_dup = User(**dict_model)
        self.assertDictEqual(model.to_dict(), model_dup.to_dict())
        self.assertIsNot(model, model_dup)
        self.assertIsInstance(model_dup, User)


if __name__ == '__main__':
    unittest.main()
