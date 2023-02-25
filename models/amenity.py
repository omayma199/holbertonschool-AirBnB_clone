#!/usr/bin/python3
"""class amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """inherited class Amenity from BaseModel"""
    name = ""
    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)