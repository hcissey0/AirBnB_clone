#!/usr/bin/python3
"""This is the review class"""

from .base_model import BaseModel


class Review(BaseModel):
    """This is the review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
