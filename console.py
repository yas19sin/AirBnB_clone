#!/usr/bin/python3
""" Console module for AirBnB """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the console AirBnB"""
    prompt = "(hbnb) "

    g_Classes = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    g_Strings = ["name", "amenity_id", "place_id", "state_id",
                 "user_id", "city_id", "description", "text",
                 "email", "password", "first_name", "last_name"]
    g_Intgers = ["number_rooms", "number_bathrooms",
                 "max_guest", "price_by_night"]

    g_Flots = ["latitude", "longitude"]

    def do_EOF(self, arg):
        """Ctrl-D to exit the program\n"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance :
Usage: create <class name>\n"""
        i_Classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if self.valid(arg):
            gArgs = arg.split()
            if gArgs[0] in i_Classes:
                new = i_Classes[gArgs[0]]()
            storage.save()
            print(new.id)

    def do_clear(self, arg):
        """Clear data storage :
Usage: clear\n"""
        storage.all().clear()
        self.do_all(arg)
        print("** All data been clear! **")

    def valid(self, arg, _id_flag=False, _att_flag=False):
        """validation of argument that pass to commands"""
        gArgs = arg.split()
        _iLen = len(arg.split())
        if _iLen == 0:
            print("** class name missing **")
            return False
        if gArgs[0] not in HBNBCommand.g_Classes:
            print("** class doesn't exist **")
            return False
        if _iLen < 2 and _id_flag:
            print("** instance id missing **")
            return False
        if _id_flag and gArgs[0]+"."+gArgs[1] not in storage.all():
            print("** no instance found **")
            return False
        if _iLen == 2 and _att_flag:
            print("** attribute name missing **")
            return False
        if _iLen == 3 and _att_flag:
            print("** value missing **")
            return False
        return True

    def do_show(self, arg):
        """Prints the string representation of an instance
Usage: show <class name> <id>\n"""
        if self.valid(arg, True):
            gArgs = arg.split()
            _iKey = gArgs[0]+"."+gArgs[1]
            print(storage.all()[_iKey])

    def do_destroy(self, arg):
        """Deletes an instance
Usage: destroy <class name> <id>\n"""
        if self.valid(arg, True):
            gArgs = arg.split()
            _iKey = gArgs[0]+"."+gArgs[1]
            del storage.all()[_iKey]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
instances based or not on the class name
Usage1: all
Usage2: all <class name>\n"""
        gArgs = arg.split()
        _iLen = len(gArgs)
        _iList = []
        if _iLen >= 1:
            if gArgs[0] not in HBNBCommand.g_Classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if gArgs[0] in key:
                    _iList.append(str(value))
        else:
            for key, value in storage.all().items():
                _iList.append(str(value))
        print(_iList)

    def casting(self, arg):
        """cast string to float or int if possible"""
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute
Usage: update <class> <id> <attribute> \"<value>\"\n"""
        if self.valid(arg, True, True):
            gArgs = arg.split()
            _iKey = gArgs[0]+"."+gArgs[1]
            if gArgs[3].startswith('"'):
                _Excu = re.search(r'"([^"]+)"', arg).group(1)
            elif gArgs[3].startswith("'"):
                _Excu = re.search(r'\'([^\']+)\'', arg).group(1)
            else:
                _Excu = gArgs[3]
            if gArgs[2] in HBNBCommand.g_Strings:
                setattr(storage.all()[_iKey], gArgs[2], str(_Excu))
            elif gArgs[2] in HBNBCommand.g_Intgers:
                setattr(storage.all()[_iKey], gArgs[2], int(_Excu))
            elif gArgs[2] in HBNBCommand.g_Flots:
                setattr(storage.all()[_iKey], gArgs[2], float(_Excu))
            else:
                setattr(storage.all()[_iKey], gArgs[2], self.casting(_Excu))
            storage.save()

    def count(self, arg):
        """the number of instances of a class
Usage: <class name>.count()\n"""
        iCount = 0
        for key in storage.all():
            if arg[:-1] in key:
                iCount += 1
        print(iCount)

    def _exec(self, arg):
        """helper function parsing filtring replacing"""
        g_Methods = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create
        }
        _Excu = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        gArgs = _Excu[0][0]+" "+_Excu[0][2]
        _iList = gArgs.split(", ")
        _iList[0] = _iList[0].replace('"', "").replace("'", "")
        if len(_iList) > 1:
            _iList[1] = _iList[1].replace('"', "").replace("'", "")
        gArgs = " ".join(_iList)
        if _Excu[0][1] in g_Methods:
            g_Methods[_Excu[0][1]](gArgs)

    def default(self, arg):
        """default if there no command found"""
        _Excu = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        if len(_Excu) != 0 and _Excu[0][1] == "update" and "{" in arg:
            _iDict = re.search(r'{([^}]+)}', arg).group()
            _iDict = json.loads(_iDict.replace("'", '"'))
            for k, v in _iDict.items():
                _arg = arg.split("{")[0]+k+", "+str(v)+")"
                self._exec(_arg)
        elif len(_Excu) != 0:
            self._exec(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
