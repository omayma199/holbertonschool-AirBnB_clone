#!/usr/bin/python3
"""Create FileStorage Class"""
import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method all of file storage"""
        return (FileStorage.__objects)

    def new(self, obj):
        """method new of file storage"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """method save of file storage"""
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dict, file)
    
    def reload(self):
        """method reload of class reload"""
        dict = {'BaseModel':BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        try: 
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                """n_dict = json.loads(file, read())"""
                n_dict = json.load(file)
                for key, value in n_dict.items():
                    self.new(dict[value['__class__']](**value))
        except FileNotFoundError:
            pass
