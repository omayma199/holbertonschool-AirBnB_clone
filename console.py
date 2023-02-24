#!/usr/bin/python3
"""Entry point of Console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from models  import classes

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
        
    def do_create (self, args):
        """create a new instance of BaseModel"""
        if len(args) < 2:
            print('* class name missing *')
        else:
            try:
                new = eval(args)()
                new.save()
                print(new.id)
            except (NameError, SyntaxError):
                print("* class doesn't exist *")
                pass
    def do_show(self, args):
        if args == "":
            print("* class name missing *")
            pass
        else:
            store = models.storage.all()
            print(" instance id missing ")
        try:
            key = "{}.{}".format(self, args[1])
            print(str(store[key]))
        except KeyError:
            print("* class doesn't exist *")

    def do_destroy(self, arg):

        if arg == "":
            print("* class name missing *")
        else:
            store = models.storage.all()
            keys = list(store.keys())
            key = "{}.{}".format(self, arg[1])
        if key not in keys:
            print('* instance id missing *')
        else:
            del store[key]
            models.storage.save()
        
        def do_all(self, arg):
            List = arg.split()
            if List[0] not in classes:
                print("* class doesn't exist *")
            else:
                newList = []
            for key, value in  storage.all().items():
                if value._class.name_== List[0]:
                    newList += [value._str_()]
            print(newList)

        def do_update(self, arg):
            object = models.storage.all()
            if not arg:
                print("* class name missing *")
                return 0
            elif arg[0] not in classes:
                print("* class doesn't exist *")
                return 0
            elif len(arg) < 2:
                print("* instance id missing *")
                return 0
            elif len(arg) < 3:
                print("* attribute name missing *")
                return 0
            elif len(arg) < 4:
                print("* value missing *")
                return 0

        key = "{}.{}".format(arg[0], arg[1])
        try:
            object[key]._dict_[arg[2]] = arg[3]
            models.storage.save()
        except Exception:
            print("* no instance found *")
            return 0
if _name_ == "_main_":
    HBNBCommand().cmdloop()
