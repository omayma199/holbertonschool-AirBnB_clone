#!/usr/bin/python3
"""Entry point of Console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


storage = models.storage


class HBNBCommand (cmd.Cmd):
    """Console class"""

    prompt = '(hbnb) '
    classes = {
               'BaseModel': BaseModel
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
        obj_list = []
        if List[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            newList = []
            for key, value in  storage.all().items():
                if value.__class__.__name__== List[0]:
                    newList += [value.__str__()]
            print(newList)

    def do_update(self, arg):
        """pdate an objject by className and id, with attribute and value"""
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
