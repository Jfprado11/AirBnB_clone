#!/usr/bin/python3
"""
Valid arguments id.

Define all comment atributes for other classes.
"""
import json
import uuid
from datetime import datetime

class BaseModel:
    """
    Superclass BaseModel.
    """
    def __init__(self):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = datetime.utcnow().isoformat()

    def save(self):
        """Method to save the current changes on a .json file"""
        #with open(, "w+") as file:
            #file.write(json.dumps())
        setattr(self, "updated_at", datetime.utcnow().isoformat())
    
    def to_dict(self):
        """Method to get the directory from an object"""
        new_dict= {}
        for key, value in self.__dict__.items():
            new_dict[key] = value
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """Method that return the information of the class used"""
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)
