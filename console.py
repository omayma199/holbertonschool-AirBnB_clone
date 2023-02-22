#!/usr/bin/python3
"""Entry point of Console"""
import cmd
from models.base_model import BaseModel
import models

storage = models.storage


class HBNBCommand (cmd.Cmd):
    """Console class"""

    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg) :
        """quit command"""
        return  True

    def do_EOF(self, arg):
        """end of file"""
        print()
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()