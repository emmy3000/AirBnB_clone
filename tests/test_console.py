#!/usr/bin/python3

import os
import sys
import unittest

from io import StringIO
from unittest.mock import patch
from .models import storage
from .models.engine.file_storage impory FileStorage
from .console import HBNCommand

class TestHBNBCommandPrompting(unittest.TestCase):
    """
    Unittests for testing prompt functionalities of the
    HBNB command interpreter
    """

    @classmethod
    def setUpClass(self):
        """
        Set up any necessary resources for the test case.
        """
        self.command_interpreter = HBNBCommand()
    
    @classmethod
    def tearDownClass(self):
        """
        Clean up any resources after the test class.
        """
        pass

    def test_prompt_string(self):
        """
        Tests to note that prompt string is correct
        """
        expected_prompt = "(hbnb) "
        self.assertEqual(expected_prompt, self.command_interpreter.prompt)

    def test_empty_line_behaviour(self):
        """
        Tests the behaviour when an empty line is entered.
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HNBCommand()
            command_interpreter.onecmd("")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)


class TestHBNBCommandHelp(unittest.TestCase):
    """
    Unittests for testing help messages of the HBNB command interpreter.
    """

    def test_help_quit_command(self):
        """
        Tests the help message for the quit command.
        """
        expected_output = "Quit command: Exit the program."
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help quit")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(expected_output, actual output)

    def test_help_create_command(self):
        """
        Tests help message for the create command.
        """
        expected_output = (
                "Usage: create <class>\n"
                "       Create a new instance of the specified class and print its id."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help create")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(expected_output, actual_output)
            
    def test_help_EOF_command(self):
        """
        Tests help message for the EOF command.
        """
        expected_output = "EOF command: Exit the program."
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter - HBNBCommand()
            command_interpreter.onecmd("help EOF")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(expected_output, actual_output)

    def test_help_command(self):
        """
        Tests help message for the show command.
        """
        expected_output = (
                "Usage: show <class> <id> or <class>.show(<id>)\n"
                "       Display the string representation of a class instance with the given id"
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help show")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(expected_output, actual_output)

    def test_help_destroy_command(self):
        """
        Tests help message for the destroy command.
        """
        expected_output = (
                "Usage: destroy <class> <id> or <class>.destroy(<id>)\n"
                "       Delete a class instance with the given id."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help destroy")
            self.assertFalse(actual_output)
            self.assertEqual(expected_output, actual_output)

    def test_help_all_command(self):
        """
        Tests help message for the all command.
        """
        expected_output = (
                "Usage: all or all <class> or <class>.all()\n"
                "       Display string representations of all instances of a given class.\n"
                "       If no class is specified, displays all instantiated objects."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(expected_output, mock_output.getvalue().strip())

    def test_help_count_command(self):
        """
        Tests help message for the count command.
        """
        expected_output = (
                "Usage: count <class> or <class>.count()\n"
                "       Retrieve the number of instances of given class."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(expected_output, mock_output.getvalue().strip())

    def test_help_update_command(self):
        """
        Tests help message for the update command.
        """
        expected_output = (
                "Usage: update <class> <id> <attribute_name> <attribute_value> or\n"
                "       <class>.update(<id>, <attribute_name>, <attribute_value> or\n"
                "       <class>.update(<id>, <dictionary>)\n"
                "       Update a class instance of a given id by adding or updating\n"
                "       a given attribute key/value pair or dictionary."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(exoect_output, mock_output.getvalue().strip())

    def test_help_general(self):
        """
        Tests help message for the general help command.
        """
        expected_output = (
                "Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF all count create destroy help quit show update"
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(expected_output, mock_output.getvalue().strip())

class TestHBNBCommandExit(unittest.TestCase):
    """
    Unittests for testing `exit` from the HBNB command interpreter.
    """

    def test_quit_command_exits(self):
        """
        Tests the `quit` command for exiting the command interpreter.
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("quit")
            self.assertTrue(result)

    def test_EOF_command_exits(self):
        """
        Tests the `EOF` command exits the command interpreter.
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("EOF")
            self.assertTrue(result)

class TestHBNBCommandCreate(unittest.TestCase):
    """
    Unittests for testing the `create` command in the HBNB command intepreter
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test environment before running test case.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test environment after running test case.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class_name(self):
        """
        Tests creating an instance without providing a class name.
        """
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("create")
            self.assertFalse(result)
            self.assertEqual(expected_output, mock_output.getvalue().strip())

    def test_create_invalid_class_name(self):
        """
        Tests creating an instance with an invalid class name.
        """
        expected_output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("create MyModel")
            self.assertFalse(result)
            self.assertEqual(expected_output, mock_output.getvalue().strip())

    def test_create_invalid_syntax(self):
        """
        Tests creating an instance with invalid syntax.
        """
        expected_output = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("MyModel.create()")
            self.assertFalse(result)
            self.assertEqual(expected_output, mock_output.getvalue().strip())

        expected_output ="*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter =HBNBCommand()
            result = command_interpreter,onecmd("BaseModel.create()")
            self.assertFalse(result)
            self.assertEqual(expected_output, mock_output.getvalue().strip())

    def test_create_object(self):
        """
        Tests creating instances of different classes using the `create` command.
        """

