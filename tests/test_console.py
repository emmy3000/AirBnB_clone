#!/usr/bin/python3

import os
import sys
import unittest

from io import StringIO
from unittest.mock import patch
from .models import storage
from .models.engine.file_storage import FileStorage
from .console import HBNBCommand


class TestHBNBCommandPrompting(unittest.TestCase):
    """
    Unit tests for testing the prompt functionalities
    of the HBNB command interpreter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up any necessary resources for the test class.
        """
        cls.command_interpreter = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        Clean up any resources after the test class.
        """
        pass

    def test_prompt_string(self):
        """
        Tests if the prompt string is correctly set.
        """
        actual_prompt = "(hbnb) "
        self.assertEqual(actual_prompt, self.command_interpreter.prompt)

    def test_empty_line_behavior(self):
        """
        Test the behaviour when an empty line is entered.
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)


class TestHBNBCommandHelp(unittest.TestCase):
    """
    Unit tests for testing help messages of the HBNB command interpreter.
    """

    def test_help_quit_command(self):
        """
        Tests help message for the quit command.
        """
        actual_output = "Quit command: Exit the program."
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help quit")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(actual_output, mock_output)

    def test_help_create_command(self):
        """
        Tests help message for the create command.
        """
        actual_output = (
            "Usage: create <class >\n"
            "       Create a new instance of the specified class
            and print its id."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help create")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(actual_output, mock_output)

    def test_help_EOF_command(self):
        """
        Tests help message for the EOF command.
        """
        actual_output = "EOF command: Exit the program."
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help EOF")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(actual_output, mock_output)

    def test_help_show_command(self):
        """
        Tests help message for the show command.
        """
        actual_output = (
            "Usage: show <class > <id > or <class >.show( <id >)\n"
            "       Display the string representation of a class instance\
            with the given id."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help show")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(actual_output, mock_output)

    def test_help_destroy_command(self):
        """
        Tests help message for the destroy command.
        """
        actual_output = (
            "Usage: destroy <class > <id > or <class >.destroy( <id >)\n"
            "       Delete a class instance with the given id."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            command_interpreter.onecmd("help destroy")
            actual_output = mock_output.getvalue().strip()
            self.assertFalse(actual_output)
            self.assertEqual(actual_output, mock_output)

    def test_help_all_command(self):
        """
        Tests help message for the all command.
        """
        actual_output = (
            "Usage: all or all <class > or <class >.all()\n"
            " Display string representations of all instances\
            of a given class .\n"
            "       If no class is specified, displays all\
            instantiated objects."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(actual_output, mock_output.getvalue().strip())

    def test_help_count_command(self):
        """
        Tests help message for the count command.
        """
        actual_output = (
            "Usage: count <class > or <class >.count()\n"
            "       Retrieve the number of instances of a given class."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(actual_output, mock_output.getvalue().strip())

    def test_help_update_command(self):
        """
        Tests help message for the update command.
        """
        actual_output = (
                "Usage: update <class> <id> <attr_name> <attr_value> or\n"
                "   <class>.update(<id>, <attr_name>, <attr_value>) or\n"
                "   <class>.update(<id>, <dict>)\n"
                "Update a class instance of a given id by adding or updating\n"
                "a given attribute key/value pair or dictionary."
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(actual_output, mock_output.getvalue().strip())

    def test_help_general(self):
        """
        Tests help message for the general help command.
        """
        actual_output = (
            "Documented commands (type help <topic >): \n"
            " == == == == == == == == == == == == == == == == == == == ==\n"
            "EOF all count create destroy help quit show update"
        )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(actual_output, mock_output.getvalue().strip())


class TestHBNBCommandExit(unittest.TestCase):
    """
    Unit tests for testing exiting from the HBNB command interpreter.
    """

    def test_quit_command_exits(self):
        """
        Tests the 'quit' command exits the command interpreter.
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("quit")
            self.assertTrue(result)

    def test_EOF_command_exits(self):
        """
        Tests the 'EOF' command exits the command interpreter.
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("EOF")
            self.assertTrue(result)


class TestHBNBCommandCreate(unittest.TestCase):
    """
    Unit tests for testing the 'create' command in the HBNB
    command interpreter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test environment before running the test cases.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """
        Tears down the test environment after running the test cases.
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
        actual_output = " ** class name missing * *"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            command_interpreter = HBNBCommand()
            result = command_interpreter.onecmd("create")
            self.assertFalse(result)
            self.assertEqual(actual_output, mock_output.getvalue().strip())

    def test_create_invalid_class_name(self):
        """
        Tests creating an instance with an invalid class name.
        """
        actual_output = " ** class doesn't exist * *"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(actual_output, mock_output.getvalue().strip())

    def test_create_invalid_syntax(self):
        """
        Tests creating an instance with invalid syntax.
        """
        actual_output = " ** * Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(
                    actual_output, mock_output.getvalue().strip()
            )

        actual_output = " ** * Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(
                    actual_output, mock_output.getvalue().strip()
            )

    def test_create_instances_of_different_classes(self):
        """
        Tests creating instances of different classes using
        the 'create' command.
        """
        classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
        ]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                command_interpreter = HBNBCommand()
                result = command_interpreter.onecmd(
                    "create {}".format(class_name))
                self.assertFalse(result)
                self.assertLess(0, len(mock_output.getvalue().strip()))
                test_key = "{}.{}".format(
                    class_name, mock_output.getvalue().strip())
                self.assertIn(test_key, storage.all().keys())


class TestHBNBCommandShow(unittest.TestCase):
    """
    Unit tests for testing the 'show' command
    in the HBNB command interpreter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up class method to prepare for the test case.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """
        Tears down class method to clean up after the test case.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        """
        Tests showing an instance with a missing class name.
        """
        actual_output = "** class name missing **"
        commands = ["show", ".show()"]

        for cmd in commands:
            with self.subTest(cmd=cmd):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(HBNBCommand().onecmd(cmd))
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_invalid_class(self):
        """
        Tests showing an instance with an invalid class name.
        """
        actual_output = "** class doesn't exist **"
        commands = ["show MyModel", "MyModel.show()"]

        for cmd in commands:
            with self.subTest(cmd=cmd):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(HBNBCommand().onecmd(cmd))
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_missing_id_space_notation(self):
        """
        Tests showing an instance with a missing ID using space notation.
        """
        actual_output = "** instance id missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for cls in classes:
            with self.subTest(cls=cls):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(HBNBCommand().onecmd(f"show {cls}"))
                    self.assertEqual(
                            actual_output, mock_outputoutput.getvalue().strip()
                    )

    def test_show_missing_class(self):
        """
        Tests showing an instance with a missing class name.
        """
        actual_output = "** class name missing **"
        commands = ["show", ".show()"]

        for cmd in commands:
            with self.subTest(cmd=cmd):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(HBNBCommand().onecmd(cmd))
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_invalid_class(self):
        """
        Tests showing an instance with an invalid class name.
        """
        actual_output = "** class doesn't exist **"
        commands = ["show MyModel", "MyModel.show()"]

        for cmd in commands:
            with self.subTest(cmd=cmd):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(HBNBCommand().onecmd(cmd))
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_missing_id_space_notation(self):
        """
        Tests showing an instance with a missing ID using space notation.
        """
        actual_output = "** instance id missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for cls in classes:
            with self.subTest(cls=cls):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(HBNBCommand().onecmd(f"show {cls}"))
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_missing_id_dot_notation(self):
        """
        Tests showing an instance with a missing ID using dot notation.
        """
        actual_output = "** instance id missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for cls in classes:
            with self.subTest(cls=cls):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(
                            HBNBCommand().onecmd(f"{cls}.show()")
                    )
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_no_instance_found_space_notation(self):
        """
        Test showing an instance that doesn't exist using space notation.
        """
        actual_output = "** no instance found **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for cls in classes:
            with self.subTest(cls=cls):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(
                            HBNBCommand().onecmd(f"show {cls} 1")
                    )
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_no_instance_found_dot_notation(self):
        """
        Test showing an instance that doesn't exist using dot notation.
        """
        actual_output = "** no instance found **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for cls in classes:
            with self.subTest(cls=cls):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(HBNBCommand().onecmd(f"{cls}.show(1)"))
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_show_objects_space_notation(self):
        """
        Test showing existing objects using space notation.
        """
        classes = [
                "BaseModel",
                "User",
                "State",
                "Place",
                "City",
                "Amenity",
                "Review"
        ]

        for cls in classes:
            with self.subTest(cls=cls):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(
                            HBNBCommand().onecmd(f"create {cls}")
                    )
                    testID = mock_output.getvalue().strip()

                with patch("sys.stdout", new=StringIO()) as mock_output:
                    obj = storage.all()[f"{cls}.{testID}"]
                    command = f"show {cls} {testID}"
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertEqual(
                            obj.__str__(), mock_output.getvalue().strip()
                    )

    def test_show_missing_id_space_notation(self):
        """
        Tests show command with missing instance ID (space notation).
        """
        actual_output = "** instance id missing **"
        commands = [
            "show BaseModel",
            "show User",
            "show State",
            "show City",
            "show Amenity",
            "show Place",
            "show Review"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                result = HBNBCommand().onecmd(command)
                self.assertFalse(result)
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_show_missing_id_dot_notation(self):
        """
        Test show command with missing instance ID (dot notation).
        """
        actual_output = "** instance id missing **"
        commands = [
            "BaseModel.show()",
            "User.show()",
            "State.show()",
            "City.show()",
            "Amenity.show()",
            "Place.show()",
            "Review.show()"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                result = HBNBCommand().onecmd(command)
                self.assertFalse(result)
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_show_no_instance_found_space_notation(self):
        """
        Tests show command with no instance found (space notation).
        """
        actual_output = "** no instance found **"
        commands = [
            "show BaseModel 1",
            "show User 1",
            "show State 1",
            "show City 1",
            "show Amenity 1",
            "show Place 1",
            "show Review 1"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                result = HBNBCommand().onecmd(command)
                self.assertFalse(result)
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_show_no_instance_found_dot_notation(self):
        """
        Tests show command with no instance found (dot notation).
        """
        actual_output = "** no instance found **"
        commands = [
            "BaseModel.show(1)",
            "User.show(1)",
            "State.show(1)",
            "City.show(1)",
            "Amenity.show(1)",
            "Place.show(1)",
            "Review.show(1)"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                result = HBNBCommand().onecmd(command)
                self.assertFalse(result)
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_show_objects_space_notation(self):
        """
        Test show command for existing objects (space notation).
        """
        commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(HBNBCommand().onecmd(command))
                obj_id = mock_output.getvalue().strip()

            obj_type = command.split(" ")[1]
            obj = storage.all()["{}.{}".format(obj_type, obj_id)]

            with patch("sys.stdout", new=StringIO()) as mock_output:
                show_command = "show {} {}".format(obj_type, obj_id)
                self.assertFalse(HBNBCommand().onecmd(show_command))
                self.assertEqual(
                        obj.__str__(), mock_output.getvalue().strip()
                )

    def test_destroy_id_missing_dot_notation(self):
        """
        Test 'destroy' command with missing instance ID (dot notation).
        """
        actual_output = "** instance id missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd(f"{class_name}.destroy()")
                )
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_destroy_invalid_id_space_notation(self):
        """
        Test 'destroy' command with invalid instance ID (space notation).
        """
        actual_output = "** no instance found **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(
                        HBNBCommand().onecmd(f"destroy {class_name} 1")
                )
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_destroy_invalid_id_dot_notation(self):
        """
        Test 'destroy' command with invalid instance ID (dot notation).
        """
        actual_output = "** no instance found **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd(f"{class_name}.destroy(1)")
                )
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_destroy_objects_space_notation(self):
        """
        Test 'destroy' command for existing objects (space notation).
        """
        commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd(command)
                )
                test_id = mock_output.getvalue().strip()

            class_name = command.split(" ")[1]
            obj_key = "{}.{}".format(class_name, test_id)

            with patch("sys.stdout", new=StringIO()) as mock_output:
                obj = storage.all()[obj_key]
                command = "destroy {} {}".format(class_name, test_id)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
                """
                Additional assertion to check if the object is destroyed
                """
                self.assertNotIn(obj_key, storage.all())

    def test_destroy_objects_dot_notation(self):
        """
        Test 'destroy' command for existing objects (dot notation).
        """
        commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(HBNBCommand().onecmd(command))
                test_id = mock_output.getvalue().strip()

            class_name = command.split(" ")[1]
            obj_key = "{}.{}".format(class_name, test_id)

            with patch("sys.stdout", new=StringIO()) as mock_output:
                obj = storage.all()[obj_key]
                command = "{}.destroy({})".format(class_name, test_id)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
                """
                Additional assertion to check if the object is destroyed
                """
                self.assertNotIn(obj_key, storage.all())


class TestHBNBCommandDestroy(unittest.TestCase):
    """
    Unit tests for the 'destroy' command in the HBNB command interpreter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up class method to prepare for the test case.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """
        Tears down class method to clean up after the test case.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_missing_class(self):
        """
        Tests 'destroy' command with missing class name.
        """
        actual_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(
                    actual_output, mock_output.getvalue().strip()
            )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(
                    actual_output, mock_output.getvalue().strip()
            )

    def test_destroy_invalid_class(self):
        """
        Tests 'destroy' command with invalid class name.
        """
        actual_output = "** class doesn't exist **"
        classes = ["MyModel"]

        for class_name in classes:
            with self.subTest(class_name=class_name):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(
                            HBNBCommand().onecmd(f"destroy {class_name}")
                    )
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(
                            HBNBCommand().onecmd(f"{class_name}.destroy()")
                    )
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_destroy_id_missing_space_notation(self):
        """
        Tests 'destroy' command with missing instance ID (space notation).
        """
        actual_output = "** instance id missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for class_name in classes:
            with self.subTest(class_name=class_name):
                with patch("sys.stdout", new=StringIO()) as mock_output:
                    self.assertFalse(
                            HBNBCommand().onecmd(f"destroy {class_name}")
                    )
                    self.assertEqual(
                            actual_output, mock_output.getvalue().strip()
                    )

    def test_destroy_id_missing_dot_notation(self):
        """
        Tests 'destroy' command with missing instance ID (dot notation).
        """
        actual_output = "** instance id missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd(f"{class_name}.destroy()")
                )
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_destroy_invalid_id_space_notation(self):
        """
        Tests 'destroy' command with invalid instance ID (space notation).
        """
        actual_output = "** no instance found **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd(f"destroy {class_name} 1")
                )
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_destroy_invalid_id_dot_notation(self):
        """
        Tests 'destroy' command with invalid instance ID (dot notation).
        """
        actual_output = "** no instance found **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd(f"{class_name}.destroy(1)")
                )
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_destroy_objects_space_notation(self):
        """
        Tests 'destroy' command for existing objects (space notation).
        """
        commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(HBNBCommand().onecmd(command))
                test_id = mock_output.getvalue().strip()

            class_name = command.split(" ")[1]
            obj_key = "{}.{}".format(class_name, test_id)

            with patch("sys.stdout", new=StringIO()) as mock_output:
                obj = storage.all()[obj_key]
                command = "destroy {} {}".format(class_name, test_id)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
                """
                Additional assertion to check if the object is destroyed
                """
                self.assertNotIn(obj_key, storage.all())

    def test_destroy_objects_dot_notation(self):
        """
        Tests 'destroy' command for existing objects (dot notation).
        """
        commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for command in commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(HBNBCommand().onecmd(command))
                test_id = mock_output.getvalue().strip()

            class_name = command.split(" ")[1]
            obj_key = "{}.{}".format(class_name, test_id)

            with patch("sys.stdout", new=StringIO()) as mock_output:
                obj = storage.all()[obj_key]
                command = "{}.destroy({})".format(class_name, test_id)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
                """
                Additional assertion to check if the object is destroyed
                """
                self.assertNotIn(obj_key, storage.all())


class TestHBNBCommandAll(unittest.TestCase):
    """
    Unit tests for testing the 'all' command in the HBNB command interpreter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class enviroment.
        """
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """
        Tears down the test class environment.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_all_invalid_class(self):
        """
        Tests 'all' command with an invalid class.
        """
        actual_output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(
                    actual_output, mock_output.getvalue().strip()
            )
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(
                    actual_output, mock_output.getvalue().strip()
            )

    def test_all_objects_space_notation(self):
        """
        Tests 'all' command for existing objects using space notation.
        """
        create_commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for create_command in create_commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(HBNBCommand().onecmd(create_command))

        actual_classes = [
                "BaseModel",
                "User",
                "State",
                "Place",
                "City",
                "Amenity",
                "Review"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            output_lines = mock_output.getvalue().strip().split("\n")

            for expected_class in actual_classes:
                with self.subTest(class_name=expected_class):
                    self.assertIn(expected_class, mock_output_lines)

    def test_all_single_object_space_notation(self):
        """
        Tests 'all' command for a single object using space notation.
        """
        create_commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for create_command in create_commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(HBNBCommand().onecmd(create_command))

        actual_classes = [
                "BaseModel",
                "User",
                "State",
                "Place",
                "City",
                "Amenity",
                "Review"
        ]
        for class_name in actual_classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd("all {}".format(class_name))
                )
                self.assertIn(class_name, mock_output.getvalue().strip())
                for other_class in actual_classes:
                    if other_class != class_name:
                        self.assertNotIn(
                                other_class, mock_output.getvalue().strip()
                        )

    def test_all_single_object_dot_notation(self):
        """
        Tests 'all' command for a single object using dot notation.
        """
        create_commands = [
            "create BaseModel",
            "create User",
            "create State",
            "create Place",
            "create City",
            "create Amenity",
            "create Review"
        ]

        for create_command in create_commands:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(HBNBCommand().onecmd(create_command))

        actual_classes = [
                "BaseModel",
                "User",
                "State",
                "Place",
                "City",
                "Amenity",
                "Review"
        ]
        for class_name in actual_classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                self.assertFalse(
                        HBNBCommand().onecmd("{}.all()".format(class_name))
                )
                self.assertIn(class_name, mock_output.getvalue().strip())
                for other_class in actual_classes:
                    if other_class != class_name:
                        self.assertNotIn(
                                other_class, mock_output.getvalue().strip()
                        )


class TestHBNBCommandUpdate(unittest.TestCase):
    """
    Unittests for testing the 'update' command
    in the HBNB command interpreter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class environment.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """
        Tears down the test class.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_class_name(self):
        """
        Tests 'update' command with missing class name.
        """
        proper_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(
                    proper_output, mcok_output.getvalue().strip()
            )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(
                    proper_output, mock_output.getvalue().strip()
            )

    def test_update_invalid_class_name(self):
        """
        Tests 'update' command with invalid class name.
        """
        proper_output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(correct_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(correct_output, output.getvalue().strip())

    def test_update_missing_id_space_notation(self):
        """
        Tests 'update' command with missing id (space notation).
        """
        proper_output = "** instance id missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                self.assertFalse(
                        HBNBCommand().onecmd(f"update {class_name}")
                )
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_missing_id_dot_notation(self):
        """
        Tests 'update' command with missing id (dot notation).
        """
        proper_output = "** instance id missing **"
        classes = ["BaseModel", "User"]
        with patch("sys.stdout", new=StringIO()) as output:
            for class_name in classes:
                self.assertFalse(
                        HBNBCommand().onecmd(f"{class_name}.update()")
                )
                self.assertEqual(
                        correct_output, output.getvalue().strip()
                )

    def test_update_invalid_id_space_notation(self):
        """
        Tests 'update' command with invalid id (space notation).
        """
        proper_output = "** no instance found **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_ output:
            for class_name in classes:
                self.assertFalse(
                        HBNBCommand().onecmd(f"update {class_name} 1")
                )
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_invalid_id_dot_notation(self):
        """
        Tests 'update' command with invalid id (dot notation).
        """
        actual_output = "** no instance found **"
        classes = ["BaseModel", "User"]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                self.assertFalse(
                        HBNBCommand().onecmd(f"{class_name}.update(1)")
                )
                self.assertEqual(
                        actual_output, mock_output.getvalue().strip()
                )

    def test_update_missing_attr_name_space_notation(self):
        """
        Tests 'update' command with missing attribute name (space notation).
        """
        proper_output = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place"]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                testId = mock_output.getvalue().strip()
                testCmd = f"update {class_name} {testId}"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_missing_attr_name_dot_notation(self):
        """
        Tests 'update' command with missing attribute name (dot notation).
        """
        proper_output = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place"]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                testId = mock_output.getvalue().strip()
                testCmd = f"{class_name}.update({testId})"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(proper_output, mock_output.getvalue().strip())

    def test_update_missing_attr_value_space_notation(self):
        """
        Tests 'update' command with missing attribute value (space notation).
        """
        proper_output = "** value missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = mock_output.getvalue().strip()
                testCmd = f"update {class_name} {testId} attr_name"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_missing_attr_value_dot_notation(self):
        """
        Tests 'update' command with missing attribute value (dot notation).
        """
        proper_output = "** value missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = mock_output.getvalue().strip()
                testCmd = f"{class_name}.update({testId}, attr_name)"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_valid_string_attr_space_notation(self):
        """
        Tests 'update' command with valid string
        attribute value (space notation).
        """
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Place",
                "Amenity",
                "Review"
        ]
        attr_name = "attr_name"
        attr_value = "attr_value"

        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = mock_output.getvalue().strip()
                testCmd = f"update {class_name} {testId}\
                            {attr_name} '{attr_value}'"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                test_dict = storage.all()[
                        f"{class_name}.{testId}"
                ].__dict__
                self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_string_attr_dot_notation(self):
        """
        Tests 'update' command with valid string
        attribute value (dot notation).
        """
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Place",
                "Amenity",
                "Review"
        ]
        attr_name = "attr_name"
        attr_value = "attr_value"

        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                tId = mock_output.getvalue().strip()
                testCmd = f"{class_name}.update({{tId}},\
                            {attr_name}, '{attr_value}')"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                test_dict = storage.all()[f"{class_name}.{tId}"].__dict__
                self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_int_attr_space_notation(self):
        """
        Tests 'update' command with valid integer
        attribute value (space notation).
        """
        classes = ["Place"]
        attr_name = "max_guest"
        attr_value = 98

        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = mock_output.getvalue().strip()
                testCmd = f"update {class_name} {{testId}}\
                            {attr_name} {attr_value}"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                test_dict = storage.all()[f"{class_name}.{testId}"].__dict__
                self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_int_attr_dot_notation(self):
        """
        Tests 'update' command with valid integer
        attribute value (dot notation).
        """
        classes = ["Place"]
        attr_name = "max_guest"
        attr_value = 98

        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                tId = mock_output.getvalue().strip()
                testCmd = f"{class_name}.update({{tId}},\
                            {attr_name}, {attr_value})"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                test_dict = storage.all()[f"{class_name}.{tId}"].__dict__
                self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_float_attr_space_notation(self):
        """
        Tests 'update' command with valid float
        attribute value (space notation).
        """
        classes = ["Place"]
        attr_name = "latitude"
        attr_value = 7.2

        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = mock_output.getvalue().strip()
                testCmd = f"update {class_name} {{testId}}\
                            {attr_name} {attr_value}"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                test_dict = storage.all()[f"{class_name}.{testId}"].__dict__
                self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_float_attr_dot_notation(self):
        """
        Tests 'update' command with valid float attribute value (dot notation).
        """
        classes = ["Place"]
        attr_name = "latitude"
        attr_value = 7.2

        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                tId = mock_output.getvalue().strip()
                testCmd = f"{class_name}.update({{tId}},\
                            {attr_name}, {attr_value})"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                test_dict = storage.all()[f"{class_name}.{tId}"].__dict__
                self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_dictionary_space_notation(self):
        """
        Tests 'update' command with valid dictionary
        attribute value (space notation).
        """
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Place",
                "Amenity",
                "Review"
        ]
        attr_name = "attr_name"
        attr_value = "attr_value"

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = mock_output.getvalue().strip()

            testCmd = f"update {class_name} {{testId}}\
                        {{{attr_name}: {attr_value}}}"
            HBNBCommand().onecmd(testCmd)

            obj_key = f"{class_name}.{testId}"
            test_dict = storage.all()[obj_key].__dict__
            self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_dictionary_dot_notation(self):
        """
        Tests 'update' command with valid dictionary attribute
        value (dot notation).
        """
        classes = [
                "BaseModel",
                "User",
                "State",
                "City", "Place",
                "Amenity",
                "Review"
        ]
        attr_name = "attr_name"
        attr_value = "attr_value"

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = mock_output.getvalue().strip()

            testCmd = f"{class_name}.update({{testId}},\
                        {{'{attr_name}': '{attr_value}'}})"
            HBNBCommand().onecmd(testCmd)

            obj_key = f"{class_name}.{testId}"
            test_dict = storage.all()[obj_key].__dict__
            self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_dictionary_with_int_space_notation(self):
        """
        Tests 'update' command with valid dictionary attribute value
        as an integer (space notation).
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            HBNBCommand().onecmd("create Place")
            testId = mock_output.getvalue().strip()

        attr_name = "max_guest"
        attr_value = 98
        testCmd = f"update Place {testId}\
                    {{'{attr_name}': {attr_value}}}"
        HBNBCommand().onecmd(testCmd)

        obj_key = f"Place.{testId}"
        test_dict = storage.all()[obj_key].__dict__
        self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_dictionary_with_int_dot_notation(self):
        """
        Tests 'update' command with valid dictionary attribute value
        as an integer (dot notation).
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            HBNBCommand().onecmd("create Place")
            testId = mock_output.getvalue().strip()

        attr_name = "max_guest"
        attr_value = 98
        testCmd = f"Place.update({{testId}},\
                    {{'{attr_name}': {attr_value}}})"
        HBNBCommand().onecmd(testCmd)

        obj_key = f"Place.{testId}"
        test_dict = storage.all()[obj_key].__dict__
        self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_dictionary_with_float_space_notation(self):
        """
        Tests 'update' command with valid dictionary attribute value
        as a float (space notation).
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            HBNBCommand().onecmd("create Place")
            testId = mock_output.getvalue().strip()

        attr_name = "latitude"
        attr_value = 9.8
        testCmd = f"update Place {testId}\
                    {{'{attr_name}': {attr_value}}}"
        HBNBCommand().onecmd(testCmd)

        obj_key = f"Place.{testId}"
        test_dict = storage.all()[obj_key].__dict__
        self.assertEqual(attr_value, test_dict[attr_name])

    def test_update_valid_dictionary_with_float_dot_notation(self):
        """
        Tests 'update' command with valid dictionary attribute value
        as a float (dot notation).
        """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            HBNBCommand().onecmd("create Place")
            testId = mock_output.getvalue().strip()

        attr_name = "latitude"
        attr_value = 9.8
        testCmd = f"Place.update({{testId}},\
                    {{'{attr_name}': {attr_value}}})"
        HBNBCommand().onecmd(testCmd)

        obj_key = f"Place.{testId}"
        test_dict = storage.all()[obj_key].__dict__
        self.assertEqual(attr_value, test_dict[attr_name])


class TestHBNBCommandUpdate(unittest.TestCase):
    """
    Unit tests for testing the 'update' command
    in the HBNB command interpreter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class environement.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """
        Tears down the test class environment.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_invalid_id_dot_notation(self):
        """
        Tests 'update' command with invalid id (dot notation).
        """
        proper_output = "** no instance found **"
        classes = ["BaseModel", "User"]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                self.assertFalse(
                        HBNBCommand().onecmd(f"{class_name}.update(1)")
                )
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_missing_attr_name_space_notation(self):
        """
        Tests 'update' command with missing
        attribute name (space notation).
        """
        proper_output = "** attribute name missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                self.assertFalse(
                        HBNBCommand().onecmd(f"create {class_name}")
                )
                test_id = mock_output.getvalue().strip()
                test_cmd = f"update {class_name} {test_id}"
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_missing_attr_name_dot_notation(self):
        """
        Tests 'update' command with missing attribute name (dot notation).
        """
        proper_output = "** attribute name missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                self.assertFalse(
                        HBNBCommand().onecmd(f"create {class_name}")
                )
                test_id = mock_output.getvalue().strip()
                test_cmd = f"{class_name}.update({test_id})"
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_missing_attr_value_space_notation(self):
        """
        Tests 'update' command with missing
        attribute value (space notation).
        """
        proper_output = "** value missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]
        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = mock_output.getvalue().strip()
                test_cmd = f"update {class_name} {test_id} attr_name"
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )

    def test_update_missing_attr_value_dot_notation(self):
        """
        Tests 'update' command with missing attribute value (dot notation).
        """
        proper_output = "** value missing **"
        classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        ]

        with patch("sys.stdout", new=StringIO()) as mock_output:
            for class_name in classes:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = mock_output.getvalue().strip()
                test_cmd = f"{class_name}.update({{test_id}}, attr_name)"
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(
                        proper_output, mock_output.getvalue().strip()
                )


if __name__ == "__main__":
    unittest.main()
