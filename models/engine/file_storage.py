#!/usr/bin/python3
"""
module of file engine

in this module the  serialization-deserialization
will execute for saving files
"""""""""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class FileStorage.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that willl return the dict of objects"""
        return self.__objects

    def new(self, obj):
        """set a new key in __obejcts with the key as the id"""
        name = obj.__class__.__name__
        id = obj.id
        key = name + "." + id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_dict = {}
        for key_id in self.__objects.keys():
            json_dict[key_id] = self.__objects[key_id].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """Function that returns the JSON file."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                dict_reload = json.load(f)
            for key_id in dict_reload.keys():
                class_id = key_id.split(".")
                obj = class_id[0] + "(**dict_reload[key_id])"
                self.__objects[key_id] = eval(obj)
