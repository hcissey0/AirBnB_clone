#!/usr/bin/python3
"""This is the user module or class"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is the user class for the user of the program"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
