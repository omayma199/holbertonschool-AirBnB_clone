#!/usr/bin/python3
"""Entry point of Console"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand (cmd.Cmd):
    """Console class"""

    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel
    }
