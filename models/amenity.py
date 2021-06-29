#!/usr/bin/python3
"""
Valid arguments.

Allows to save new amenity with basic information.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Class State.
        inherits from super class BaseModel.
        will hold one public class attribute
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
