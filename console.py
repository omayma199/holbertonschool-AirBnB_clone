#!/usr/bin/python3
"""Entry point of Console"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex 


storage = models.storage


class HBNBCommand (cmd.Cmd):
    """Console class"""

    prompt = '(hbnb) '
    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

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
        List = arg.split()
        obj = []
        if len(List) == 0:
            print("** class name missing **")
            return
        try:
            eval(List[0])
        except:
            print("** class doesn't exist **")
            return
        if len(List) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key_id = List[0] + "." + List[1]
            if key_id in obj:
                value = obj[key_id]
                print(value)
            else:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        List = arg.split()
        obj = []
        if len(List) == 0:
            print("** class name missing **")
            return
        try:
            eval(List[0])
        except :
            print("** class doesn't exist **")
            return
        if len(List) == 1:
            print("** instance id missing **")
        else:
            
            obj = storage.all()
            key_id = List[0] + "." + List[1]
            if key_id in obj:
                del obj[key_id]
                storage.save()
            else:
                print("** no instance found **")
        
   def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in classes:
            obj_dict = storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")
            

    def do_update(self, arg):
        List = arg.split()
        Objts =  models.storage.all()

        if len(List) == 0:
            print("** class name missing **")
            return
        elif List[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if List[0] in self.classes:
            if len(List) < 2:
                print("** instance id missing **")
                return
            value = List[0] + "." + List[1]
            if value not in Objts:
                print("** no instance found **")
            else:
                obj = Objts[value]
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
      

if __name__ == '__main__':
    HBNBCommand().cmdloop()
