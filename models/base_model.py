#!/usr/bin/python3
"""base model class."""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    The BaseModel Class
    """
    def __init__(self, *args, **kwargs):
        """
        attr(id): objectid
        attr(created_at): datetime - assign with the current datetime when an instance is created
        attr(updated_at): datetime - assign with the current datetime when an instance is created and it will be updated
        every time you change your object
        """
        if len(kwargs)  != 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    """self.__dict__[key] = value"""
                    setattr(self, key, obj)
                elif key == "updated_at":
                    obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, obj)
                elif key != "__class__":
                    setattr(self, key, value)
        
        else:
            self.id = str(uuid4())
            self.created_at =  datetime.now()
            self.updated_at= datetime.now()
            models.storage.new(self)
    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        # only when we save the instance, its writen into the json file
        models.storage.save()

    def to_dict(self):
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dic