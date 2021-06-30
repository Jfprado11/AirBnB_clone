#!/usr/bin/python3
"""Unittest for City
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Class for testing the object place"""

    def test_is_instance(self):
        """check if the rigth object is being created"""
        model = Place()
        other_model = Place()
        self.assertIsInstance(model, Place)
        self.assertEqual(len(model.id), 36)
        self.assertEqual(model.__class__.__name__, "Place")
        self.assertTrue(hasattr(model, "id"))
        self.assertNotEqual(model.id, other_model.id)
        self.assertIsInstance(model.id, str)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_setattributes(self):
        """check if the attributes are being created propertly"""
        a1 = Place()
        a1.my_number = 89
        self.assertEqual(a1.my_number, 89)
        a1.my_number = -1
        self.assertEqual(a1.my_number, -1)
        a1.my_number = 0.1
        self.assertEqual(a1.my_number, 0.1)
        # public class atributes
        self.assertTrue(hasattr(a1, 'city_id'))
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(a1.city_id, "")
        self.assertTrue(hasattr(a1, 'user_id'))
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(a1.user_id, "")
        self.assertTrue(hasattr(a1, 'name'))
        self.assertEqual(type(Place.name), str)
        self.assertEqual(a1.name, "")
        self.assertTrue(hasattr(a1, 'description'))
        self.assertEqual(type(Place.description), str)
        self.assertEqual(a1.description, "")
        self.assertTrue(hasattr(a1, 'number_rooms'))
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(a1.number_rooms, 0)
        self.assertTrue(hasattr(a1, 'number_bathrooms'))
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(a1.number_bathrooms, 0)
        self.assertTrue(hasattr(a1, 'max_guest'))
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(a1.max_guest, 0)
        self.assertTrue(hasattr(a1, 'price_by_night'))
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(a1.price_by_night, 0)
        self.assertTrue(hasattr(a1, 'latitude'))
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(a1.latitude, 0.0)
        self.assertTrue(hasattr(a1, 'longitude'))
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(a1.longitude, 0.0)
        self.assertTrue(hasattr(a1, 'amenity_ids'))
        self.assertEqual(type(Place.amenity_ids), list)
        self.assertEqual(a1.amenity_ids, [])

    def test_dict(self):
        """Test the correct implementation of the dictionary"""
        model = Place()
        dict_proper = model.to_dict()
        id_ = model.id
        time_created = model.created_at.isoformat()
        time_updated = model.updated_at.isoformat()
        dict_expected = {'__class__': 'Place', 'id': id_,
                         'updated_at': time_updated,
                         'created_at': time_created}
        self.assertDictEqual(dict_proper, dict_expected)
        model.save()
        self.assertNotEqual(time_updated, model.updated_at.isoformat())
        self.assertEqual(time_created, model.created_at.isoformat())

    def test_string_representation(self):
        """test the string represtation of the
        class BaseModel is correct"""
        model = Place()
        string = "[Place] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), string)

    def test_kwargs(self):
        """Test the right implementation if kwargs are passed"""
        model = Place()
        model.name = "alex"
        model.save()
        dict_model = model.to_dict()
        model_dup = Place(**dict_model)
        self.assertDictEqual(model.to_dict(), model_dup.to_dict())
        self.assertIsNot(model, model_dup)
        self.assertIsInstance(model_dup, Place)


if __name__ == '__main__':
    unittest.main()
