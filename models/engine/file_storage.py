#!/usr/bin/python3
"""This is the module for the storage class"""

import os


class FileStorage():
    """This is the file storage class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """This is the constructor of the FileStorage class"""
        pass

    def all(self):
        """This is the function used to access the __objects"""
        return self.__objects

    def new(self, obj):
        """adds the obj in the __objects"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes the __objects and save it to the file"""
        import json
        with open(self.__file_path, "w") as file:
            json_dict = {}
            for k, v in self.__objects.items():
                if v:
                    json_dict[k] = v.to_dict()
            json_string = json.JSONEncoder().encode(json_dict)
            file.write(json_string)

    def reload(self):
        """Reloads the json string form the file to __objects"""
        import json
        from ..base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_string = file.read()
                if len(json_string) > 0:
                    json_dict = json.JSONDecoder().decode(json_string)
                    for k, v in json_dict.items():
                        self.__objects[k] = BaseModel(**v)

    def delete(self, id):
        """deletes the object with the specified id"""
        if id:
            new_dict = {k: v for k, v in self.__objects.items()
                        if v.id != id}
            self.__objects = new_dict

    def update(self, id, **kwargs):
        """The update function to update an object"""
        if id:
            pass
