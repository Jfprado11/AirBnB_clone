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
from datetime import datetime


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

    def do_show(self, args):
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
        if not args:
            print("** class name missing **")
            return
        else:
            arg = args.split()
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            elif len(arg) == 1:
                print("** instance id missing **")
                return
            elif arg[0] and arg[1]:
                new_key = arg[0] + "." + arg[1]
            if any(new_key == keys for keys in created_objs.keys()):
                temp_dict = {}
                dict_insta = created_objs[new_key]
                for key, value in dict_insta.items():
                    if key == "__class__":
                        continue
                    elif key == "created_at":
                        form = '%Y-%m-%dT%H:%M:%S.%f'
                        temp_dict[key] = datetime.strptime(value, form)
                    elif key == "updated_at":
                        temp_dict[key] = datetime.strptime(value, form)
                    else:
                        temp_dict[key] = value
                print("[{}] ({}) {}".format(arg[0], arg[1], temp_dict))
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id

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
        if not args:
            print("** class name missing **")
            return
        else:
            arg = args.split()
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            elif len(arg) == 1:
                print("** instance id missing **")
                return
            elif arg[0] and arg[1]:
                new_key = arg[0] + "." + arg[1]
            if any(new_key == keys for keys in created_objs.keys()):
                created_objs.pop(new_key)
                storage.save()
            else :
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name.
            If the class name doesn’t exist it raise the following error:
                ** class doesn't exist **
        """
        new_list = []
        created_objs = storage.all()
        if not args:
            for key_id in created_objs.keys():
                temp_dict = {}
                dict_insta = created_objs[key_id]
                for key, value in dict_insta.items():
                    if key == "__class__":
                        continue
                    elif key == "created_at":
                        form = '%Y-%m-%dT%H:%M:%S.%f'
                        temp_dict[key] = datetime.strptime(value, form)
                    elif key == "updated_at":
                        temp_dict[key] = datetime.strptime(value, form)
                    else:
                        temp_dict[key] = value
                cls_insta = dict_insta["__class__"]
                id_x =  temp_dict["id"]
                str_format = "[{}] ({}) {}".format(cls_insta, id_x, temp_dict)
                new_list.append(str_format)
            print(new_list)
        else:
            if args != "BaseModel":
                print("** class doesn't exist **")

    def do_update(self):
        """
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
