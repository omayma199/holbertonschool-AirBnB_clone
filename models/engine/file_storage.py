#!/usr/bin/python3
"""Create FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dict, file)
    
    def reload(self):
        dict = {
            "BaseModel": BaseModel,
        }
        try:
            with open(self.__file_path, 'r') as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                   self.new(dict[value['__class__']](**value))
        except FileNotFoundError:
            pass
