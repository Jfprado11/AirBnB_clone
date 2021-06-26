#!/usr/bin/python3
"""
module of file engine

in this module the  serialization-deserialization
will execute for saving files
"""""""""
import json
import os


class FileStorage:
    """
    Class FileStorage.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that willl return the dict of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set a new key in __obejcts with the key as the id"""
        name = obj.__class__.__name__
        id = obj.id
        key = name + "." + id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """Function that returns the JSON file."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                dict_reload = json.load(f)
            FileStorage.__objects = dict_reload
