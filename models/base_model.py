#!/usr/bin/python3
"""
Module will hold the class:
BaseModel
Valid arguments.

Define all common atributes for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Superclass BaseModel.
    holds four public methods:
        __init__ = the constructor of the class
        save = will save any change for the class
        to dict = return a form representation of the class
        __str__ = construct the given string represetation
    """

    def __init__(self, *args, **kwargs):
        """the initialization of the instaces atributes
        attrs:
            self.id (id) = string that gives to each instances a unique id
            self.created_at = gives a time when the intances was created
            self.uptated_at = gives a time when a object of the instaces
            were change
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Method to save the current changes on a .json file
        also will change the atribute "updated_at" with a new datetime value
        """
        setattr(self, "updated_at", datetime.now())
        models.storage.save()

    def to_dict(self):
        """Method to get the directory from an object
        for atributtes "created_at" and "updated_at":
            will convert the object datetime into a string represetation
        and will add the key "__class__" holding the class name of the object
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at":
                new_dict[key] = self.created_at.isoformat()
            elif key == "updated_at":
                new_dict[key] = self.updated_at.isoformat()
            else:
                new_dict[key] = value

        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """Method that return the information of the class used"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
