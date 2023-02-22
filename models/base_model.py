#!/usr/bin/python3
"""
Base Module
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base Class
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['updated_at'] = self.updated_at.isoformat()
        dict['created_at'] = self.created_at.isoformat()
        return dict
