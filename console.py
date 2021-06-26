#!/usr/bin/python3
"""
module that will run the console
for project clone AirBnB holds a package,
cmd that will be used for creating the command line
imterpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class will hold the cmd module
    that will used for running the command line enterpreter
    """
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
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
        anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
