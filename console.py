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
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class will hold the cmd module
    that will used for running the command line enterpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Command to exit the prompt directly
        """
        return True

    def do_EOF(self, arg):
        """Allows to exit the prompt by typing ctrl^d
        """
        print()
        return True

    def emptyline(self):
        """When a empty line is passed, does not do
        anything""""""
        """
        pass

    def default(self, line: str) -> bool:
        """default value when it not recognice returns
        the erros else while print the requeriment
        """
        created_objs = storage.all()
        all = ["BaseModel.count()", "User.count()",
               "Place.count()", "City.count()",
               "State.count()", "Amenity.count()", "Review.count()"]
        if line in all:
            trim = line.split(".")
            number = 0
            for key_id in created_objs.keys():
                num = key_id.rfind(trim[0])
                if num != -1:
                    number = number + 1
            print(number)

        else:
            return super().default(line)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and print his id.

            If the class name is missing it raise the following error:
                ** class name missing **

            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **
        """
        models = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place", "Review"]
        if not arg:
            print("** class name missing **")
        elif arg not in models:
            print("** class doesn't exist **")
        else:
            arg = arg + "()"
            obj = eval(arg)
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id

            If the class name is missing it raise the following error:
                ** class name missing **

            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **

            If the id is missing it raise the following error:
                ** instance id missing **

            If the instance of the class name doesn’t exist for the
            id it raise the following error:
                ** no instance found **
        """
        created_objs = storage.all()
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        if not arg:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if not args[0] in models:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif args[0] and args[1]:
                new_key = args[0] + "." + args[1]
            if any(new_key == keys for keys in created_objs.keys()):
                print(created_objs[new_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id

            If the class name is missing it raise the following error:
                ** class name missing **

            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **

            If the id is missing it raise the following error:
                ** instance id missing **

            If the instance of the class name doesn’t exist for
            the id it raise the following error:
                ** no instance found **
        """
        created_objs = storage.all()
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        if not arg:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if not args[0] in models:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif args[0] and args[1]:
                new_key = args[0] + "." + args[1]
            if any(new_key == keys for keys in created_objs.keys()):
                created_objs.pop(new_key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name.
            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **
        """
        new_list = []
        created_objs = storage.all()
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        if not arg:
            for key_id in created_objs.keys():
                new_list.append(created_objs[key_id].__str__())
            print(new_list)
        else:
            if arg not in models:
                print("** class doesn't exist **")
            else:
                for key_id in created_objs.keys():
                    num = key_id.rfind(arg)
                    if num != -1:
                        new_list.append(created_objs[key_id].__str__())
                print(new_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute

            Usage:
            update <class name> <id> <attribute name> "<attribute value>"

            If the class name is missing it raise the following error:
                ** class name missing **

            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **

            If the id is missing it raise the following error:
                ** instance id missing **

            If the instance of the class name doesn’t exist
            for the id it raise the following error:
                ** no instance found **

            If the attribute name is missing it raise the following error:
                ** attribute name missing **

            If the value for the attribute name doesn’t exist it
            raise the following error:
                ** value missing **
        """
        if not arg:
            print("** class name missing **")
        else:
            created_objs = storage.all()
            models = ["BaseModel", "User", "State", "City",
                      "Amenity", "Place", "Review"]
            args = arg.split()
            if not args[0] in models:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            if args[0] and args[1]:
                new_key = args[0] + "." + args[1]
            if any(new_key == keys for keys in created_objs.keys()):
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
                if len(args) == 3:
                    print("** value missing **")
                    return
                obj = created_objs[new_key]
                trim = args[3]
                trim = trim[1:-1]
                try:
                    trim = int(trim)
                except:
                    try:
                        trim = float(trim)
                    except:
                        trim = str(trim)
                setattr(obj, args[2], trim)
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
