#!/usr/bin/python3
"""Entry point of Console"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



storage = models.storage


class HBNBCommand (cmd.Cmd):
    """Console class"""

    prompt = '(hbnb) '
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def emptyline(self):
        pass

    def do_quit(self, arg) :
        """quit command"""
        return  True

    def do_EOF(self, arg):
        """end of file"""
        print()
        return True
        
    def do_create (self, arg):
        """create a new instance of BaseModel"""
        List = arg.split()
        if arg == "" :
            print('** class name missing **')
        else:
            try:
                new = eval(List[0])()
                new.save()
                print(new.id)
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
                
    def do_show(self, arg):
        """show object by id"""
        List = arg.split(arg)
        if len(List) == 0:
            print("** class name missing **")
            return False
        if List[0] in classes:
            if len(List) > 1:
                key = Lists[0] + "." + Lists[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        lists = arg.split()
        obj = []
        if len(lists) == 0:
            print("** class name missing **")
            return
        try:
            eval(lists[0])
        except :
            print("** class doesn't exist **")
            return
        if len(lists) == 1:
            print("** instance id missing **")
        else:
            
            obj = storage.all()
            key_id = lists[0] + "." + lists[1]
            if key_id in obj:
                del obj[key_id]
                storage.save()
            else:
                print("** no instance found **")
        
    def do_all(self, arg):
        List = arg.split()
        obj_list = []
        if List[0] not in classes:
            print("** class doesn't exist **")
        else:
            newList = []
            for key, value in  storage.all().items():
                if value.__class__.__name__== List[0]:
                    newList += [value.__str__()]
            print(newList)

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return
        Lists = arg.split(" ")
        Objts =  storage.all()
        if Lists[0] in self.classes:
            if len(Lists) < 2:
                print("** instance id missing **")
                return
            v = Lists[0] + "." + Lists[1]
            if v not in Objts:
                print("** no instance found **")
            else:
                obj = Objts[v]
                attrbte  = ["id", "created_at", "updated_at"]
                if obj:
                    List = arg.split(" ")
                    if len(List) < 3:
                        print("** attribute name missing **")
                    elif len(List) < 4:
                        print("** value missing **")
                    elif List[2] not in attrbte:
                        obj.__dict__[List[2]] = List[3]
                        obj.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
