#!/usr/bin/python3
"""
Valid arguments.

Allows to save new city with basic information.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Class State.
        inherits from super class BaseModel.
        will hold two public class attributes
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
