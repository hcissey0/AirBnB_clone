#!/usr/bin/python3
"""This is the BaseModel class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """This is the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """This is the instantiotor method"""

        if kwargs:
            for k, v in kwargs.items():
                if not k.startswith("__"):
                    if k == "created_at":
                        self.__dict__[k] = datetime.fromisoformat(v)
                    elif k == "updated_at":
                        self.__dict__[k] = datetime.fromisoformat(v)
                    else:
                        self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """The string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This is the save funtion that saves and updates the update time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the calling object"""
        ret = dict(self.__dict__)
        ret["__class__"] = self.__class__.__name__
        ret["created_at"] = self.created_at.isoformat()
        ret["updated_at"] = self.updated_at.isoformat()
        return ret
