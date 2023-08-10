#!/usr/bin/python3
"""This is the console for the application"""

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
    """This is the console class"""

    prompt = "(hbnb) "
    models_list = ["BaseModel", "User",
                   "State", "City",
                   "Amenity", "Place",
                   "Review"]

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
                    key = ".".join(line[0:2])
                    for k, v in storage.all().items():
                        if key == k:
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
                    key = ".".join(line[0:2])
                    if key in storage.all().keys():
                        storage.delete(key)
                        storage.save()
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

    def do_update(self, line):
        """This is the update command parser"""
        if line:
            line = line.split()
            if line[0] in self.models_list:
                if len(line) > 1:
                    key = ".".join(line[0:2])
                    if key in storage.all().keys():
                        if len(line) > 2:
                            if len(line) > 3:
                                list_string = []
                                if line[3].startswith("\""):
                                    for s in line[3:]:
                                        list_string.append(s)
                                        if s.endswith("\""):
                                            break
                                    val = " ".join(list_string)
                                else:
                                    val = line[3]
                                storage.update(key,
                                               str(line[2]),
                                               eval(f"{val}"))
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_update(self):
        """The update command help desk"""
        print("Usage: update <class name> <id> <attribute name>",
              "\"<attribute value>\"\n",
              "Updates an instance based on the class name and id",
              "by adding or updating attribute",
              "(save changes to the JSON file).\nEx:",
              "$ update BaseModel 1234-1234-1234 email \"airbnb@mail.com\"\n")

    def emptyline(self):
        """this is the empty line parser"""
        pass

    def onecmd(self, line):
        """overriding the internal onecmd function"""
        args = line.split()
        exts = ["all()", "count()"]
        if len(args) > 0 and "." in args[0]:
            cmds = args[0].split(".")
            model = cmds[0]
            ext = cmds[1] if len(cmds) > 1 else ""

            if model in self.models_list:
                if ext == "all()":
                    self.do_all(model)
                    return
                elif ext == "count()":
                    print(len([k for k in storage.all().keys()
                               if k.startswith(model)]))
                    return
                elif ext.startswith("show(\"") and ext.endswith("\")"):
                    id = ext[6:-2]
                    fline = " ".join([model, id])
                    self.do_show(fline)
                    return
                elif ext.startswith("destroy(\"") and ext.endswith("\")"):
                    id = ext[9:-2]
                    fline = " ".join([model, id])
                    self.do_destroy(fline)
                    return
        return super(HBNBCommand, self).onecmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
