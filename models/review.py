#!/usr/bin/python3
"""
Valid arguments.

Allows to save new review with basic information.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Class State.
        inherits from super class BaseModel.
        will hold three public class attributes
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
