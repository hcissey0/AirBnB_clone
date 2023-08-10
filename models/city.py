#!/usr/bin/python3
"""This is the city class"""

from .base_model import BaseModel


class City(BaseModel):
    """The city class that inherits from the BaseModel class"""

    state_id = ""
    name = ""
