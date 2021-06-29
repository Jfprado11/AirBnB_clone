#!/usr/bin/python3
"""
Valid arguments.

Allows to save new state with basic information.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State.
        inherits from super class BaseModel.
        will hold one public class attributes
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
