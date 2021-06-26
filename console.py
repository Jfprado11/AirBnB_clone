#!/usr/bin/python3
"""
module that will run the console
for project clone AirBnB holds a package,
cmd that will be used for creating the command line
imterpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class will hold the cmd module
    that will used for running the command line enterpreter
    """
    prompt = '(hbnb) '
    file = None

    def do_quit(self, args):
        """Command to exit the prompt directly
        """
        return True

    def do_EOF(self, args):
        """Allows to exit the prompt by typing ctrl^d
        """
        print()
        return True

    def emptyline(self):
        """When a empty line is passed, does not do
        anything""""""
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and print his id.
            If the class name is missing it raise the following error:
                ** class name missing **
            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **
        """
        if not args:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, *args):
        """Prints the string representation of an instance based on the class name and id
            If the class name is missing it raise the following error:
                ** class name missing **
            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **
            If the id is missing it raise the following error:
                ** instance id missing **
            If the instance of the class name doesn’t exist for the id it raise the following error:
                ** no instance found **
        """
        created_objs = storage.all()
        if not args[0]:
            print("** class name missing **")
            return
        elif not args[1]:
            print("** instance id missing **")
            return
        elif args != "BaseModel":
            print("** class doesn't exist **")
            return
        elif args and args[1]:
            new_key = args + "." + args[1]
        if any(new_key == keys for keys in created_objs.keys()):
            print(new_key.to_dict())

    def do_destroy(self):
        """
        """
        pass

    def do_all(self):
        """
        """
        pass

    def do_update(self):
        """
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
