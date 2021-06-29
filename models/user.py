#!/usr/bin/python3
"""
Valid arguments.

Allows to save new users with basic information.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User.
        inherits from super class BaseModel.
        will hold four public class attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
