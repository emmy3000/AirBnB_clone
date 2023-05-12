#!/usr/bin/python3

"""
The modu;e contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D).
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def help_quit(self):
        """
        Help documentation for the quit command.
        """
        print("Quit the command interpreter.")

    def help_EOF(self):
        """
        Help documentation for the EOF command.
        """
        print("Exit the program.")

    def help_help(self):
        """
        Help documentation for the help command.
        """
        print("Show help information.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
