#!/usr/bin/python3
"""This is the console for the application"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This is the console class"""

    prompt = "(hbnb) "
    models_list = ["BaseModel"]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_quit(self):
        """The help command for the quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self, line):
        """This command creates a new BaseModel and prints the id"""
        if line:
            line = line.split()
            if line[0] in self.models_list:
                bm = eval(f"{line[0]}()")
                bm.save()
                print(bm.id)
            else:
                print("** class name doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """The help text for the create command"""
        print("Usage: create <class name>\n")
        print("Creates a new instance of BaseModel,",
              "saves it (to the JSON file) and prints",
              "the id.\nEx: $ create BaseModel\n")

    def do_show(self, line):
        """this is the show command parser"""
        if line:
            line = line.split()
            if line[0] in self.models_list:
                if len(line) > 1:
                    for v in storage.all().values():
                        if line[1] == v.id:
                            print(v)
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_show(self):
        """This is the show command help text"""
        print("Usage: show <class name> <id>\n")
        print("Prints the string representation of an instance",
              "based on the class name and id.\nEx:",
              "$ show BaseModel 1234-1234-1234\n")

    def do_destroy(self, line):
        """This is the destroy command parser"""
        obj = None
        if line:
            line = line.split()
            if line[0] in self.models_list:
                if len(line) > 1:
                    for k, v in storage.all().items():
                        if line[1] == v.id:
                            storage.delete(v.id)
                            storage.save()
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """The destroy command help desk"""
        print("Usage: destroy <class name> <id>\n")
        print("Deletes an instance based on the class name and id",
              "(save the changes into the JSON file).\nEx:",
              "$ destroy BaseModel 1234-1234-1234\n")

    def do_all(self, line):
        """Prints all the string representation of all instances"""
        all_list = []
        if line:
            line = line.split()
            if line[0] in self.models_list:
                all_list = [str(obj) for k, obj in storage.all().items()
                            if k.startswith(line[0])]
            else:
                print("** class doesn't exist **")
        else:
            all_list = [str(obj) for obj in storage.all().values()]
        if all_list:
            print(all_list)

    def help_all(self):
        """the help text for the all command"""
        print("Usage: all or all <class name>\n")
        print("Prints all string representation of all instances",
              "based or not on the class name.\nEx:",
              "$ all BaseModel or all\n")

    def emptyline(self):
        """this is the empty line parser"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
