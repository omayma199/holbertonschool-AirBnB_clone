#!/usr/bin/python3
"""State Class"""
from models.base_model import BaseModel

class State(BaseModel):
    """inherited class State from BaseModelv"""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)