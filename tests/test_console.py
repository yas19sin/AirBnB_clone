import unittest

from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestHBNBCommand_prompt(unittest.TestCase):
    """testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """testing help messages of the HBNB command interpreter."""

    def test_help(self):
        msg = ("Documented commands (type help <topic>):\n"
               "========================================\n"
               "EOF  all  clear  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_quit(self):
        msg = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_EOF(self):
        msg = "Ctrl-D to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_create(self):
        msg = ("Creates a new instance :\n"
               "Usage: create <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_show(self):
        msg = ("Prints the string representation of an instance\n"
               "Usage: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_destroy(self):
        msg = ("Deletes an instance\n"
               "Usage: destroy <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_all(self):
        msg = ("Prints all string representation of all\n"
               "instances based or not on the class name\n"
               "Usage1: all\n"
               "Usage2: all <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_update(self):
        msg = ("Updates an instance by adding or updating attribute\n"
               "Usage: update <class> <id> <attribute> \"<value>\"")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(msg, output.getvalue().strip())


class ConsoleTestCase(unittest.TestCase):
    """testing errors"""

    def check_json(self, classname, id):
        iKeyName = classname+"."+id
        with open(self.filepath, 'r') as file:
            iData = json.load(file)
        self.assertIn(iKeyName, iData)
        self.assertEqual(iData[iKeyName]["id"], id)
        self.assertEqual(iData[iKeyName]["__class__"], classname)

    def test_error(self):
        """testing errors"""
        iClassNames = ["create", "update", "show", "destroy"]

        """ class name missing """
        for cmd in iClassNames:
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class name missing **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ class doesn't exist """
        Non_Exists_class = ["create x", "update x",
                            "show x", "destroy x", "all x"]
        for cmd in Non_Exists_class:
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class doesn't exist **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ instance id missing """
        i_Cmds = ["update", "show", "destroy"]
        iClasses = HBNBCommand().g_Classes
        for cmd in i_Cmds:
            for clas in iClasses:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** instance id missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas}")
                    self.assertCountEqual(expected, f.getvalue().strip())

        """ no instance found """
        i_Cmds = ["update", "show", "destroy"]
        iClasses = HBNBCommand().g_Classes
        id_x = "x"
        for cmd in i_Cmds:
            for clas in iClasses:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** no instance found **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_x}")
                    self.assertCountEqual(expected, f.getvalue().strip())

    def test_create_object(self):
        """testing for create """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            iKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(iKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            iKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(iKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            iKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(iKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            iKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(iKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            iKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(iKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            iKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(iKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            iKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(iKey, storage.all().keys())

        """ value missing """
        new_BaseModel = BaseModel()
        new_User = User()
        new_State = State()
        new_City = City()
        new_Amenity = Amenity()
        new_Place = Place()
        new_Review = Review()
        id_BaseModel = new_BaseModel.id
        id_User = new_User.id
        id_State = new_State.id
        id_City = new_City.id
        id_Amenity = new_Amenity.id
        id_Place = new_Place.id
        id_Review = new_Review.id
        id_dict = {"BaseModel": id_BaseModel, "User": id_User,
                   "State": id_State, "City": id_City, "Amenity": id_Amenity,
                   "Place": id_Place, "Review": id_Review}
        i_Cmds = ["update"]
        iClasses = HBNBCommand().g_Classes
        for cmd in i_Cmds:
            for clas in iClasses:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** value missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]} name")
                    self.assertCountEqual(expected, f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
