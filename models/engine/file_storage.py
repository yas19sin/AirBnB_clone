#!/usr/bin/python3
"""Module for File Storage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Handles serialization and deserialization of instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        id = obj.to_dict()["id"]
        _ClassName = obj.to_dict()["__class__"]
        _KeyName = _ClassName+"."+id
        FileStorage.__objects[_KeyName] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        _pFile = FileStorage.__file_path
        iData = dict(FileStorage.__objects)
        for key, value in iData.items():
            iData[key] = value.to_dict()
        with open(_pFile, 'w') as f:
            json.dump(iData, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        _pFile = FileStorage.__file_path
        iData = FileStorage.__objects
        if os.path.exists(_pFile):
            try:
                with open(_pFile) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            iData[key] = BaseModel(**value)
                        if "User" in key:
                            iData[key] = User(**value)
                        if "Place" in key:
                            iData[key] = Place(**value)
                        if "State" in key:
                            iData[key] = State(**value)
                        if "City" in key:
                            iData[key] = City(**value)
                        if "Amenity" in key:
                            iData[key] = Amenity(**value)
                        if "Review" in key:
                            iData[key] = Review(**value)
            except Exception:
                pass
