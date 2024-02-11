#!/usr/bin/python3

"""The entry point of the command interpreter."""

from models import storage
import cmd
import models
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreters.

    Args:
        Cmd : built in class
    """
    prompt = '(hbnb) '
    b = "BaseModel"
    list_class = [b, "User", "City", "Amenity", "Place", "State", "Review"]

    list_func = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, line):
        """a method for parses command input"""

        cls = line.split('.')
        command = cls[1].split('(')
        param = command[1].split(')')
        if cls[0] in HBNBCommand.list_class and command[0] in HBNBCommand.list_func:
            line = command[0] + ' ' + cls[0] + ' ' + param[0]
        return line

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, arg):
        """to exiting the program with <Ctrl+D>"""

        print()
        quit()

    def emptyline(self):
        """to handling the emptyline"""
        pass

    def do_create(self, arg):
        """to createing a new instance
        """
        if len(arg) == 0:
            print("** class name missing **")

        elif arg not in HBNBCommand.list_class:
            print("** class doesn't exist **")

        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """a method to prints the string representation of an instance based
        on the class name and id"""

        list_args = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif list_args[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        elif len(list_args) < 2:
            print("** instance id missing **")
            return

        else:
            all_obj = storage.all()
            string = f'{list_args[0]}.{list_args[1]}'

            if string not in all_obj.keys():
                print("** no instance found **")

            else:
                print(all_obj[string])

    def do_destroy(self, arg):
        """a method to deletes an instance based on class name and id and save
        in the JSON file"""

        list_args = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif list_args[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        elif len(list_args) < 2:
            print("** instance id missing **")
            return

        else:
            all_obj = storage.all()
            string = f'{list_args[0]}.{list_args[1]}'

            if string not in all_obj.keys():
                print("** no instance found **")

            else:
                del (all_obj[string])
                storage.save()

    def do_all(self, arg):
        """a method to prints all string representation of all instances
        based or not on the class name"""

        dict_all_obj = storage.all()
        list_obj = []

        if len(arg) == 0:
            for key, vals in dict_all_obj.items():
                list_obj.append(str(vals))
            print(list_obj)

        elif arg in HBNBCommand.list_class:
            for keys, vals in dict_all_obj.items():
                if vals.__class__.__name__ == arg:
                    list_obj.append(str(vals))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """a method to Updates an instance on the class name & id by adding
        or updating attribute"""

        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")

        elif list_arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        elif len(list_arg) == 1:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            elif len(list_arg) == 2:
                print("** attribute name missing **")
                return

            elif len(list_arg) == 3:
                print("** value missing **")
                return

            else:
                setattr(dict_all_obj[string], list_arg[2], list_arg[3])
                storage.save()

    def do_count(self, arg):
        """a method to count the number of instances of a class"""

        count = 0
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            keys_split = key.split('.')
            if keys_split[0] == arg:
                count += 1
        print(count)

    def default(self, line):
        """default method"""

        cls_ = line.split('.')
        if cls_[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if cls_[1] == 'count()':
            count = 0
            for k, v in storage._FileStorage__objects.items():
                clas_part = k.split('.')[0]
                if clas_part == cls_[0]:
                    count += 1
            print(count)
            return
        if cls_[1].startswith('destroy'):
            idd = cls_[1].split('"')[1]
            ln = f"{cls_[0]} {idd}"
            self.do_destroy(ln)
            return
        if cls_[1].startswith('update') and not cls_[1].endswith('})'):
            idd = cls_[1].split('"')[1]
            att = cls_[1].split('"')[3]
            val = cls_[1].split('"')[5]
            ln = f"{cls_[0]} {idd} {att} \"{val}\""
            self.do_update(ln)
            return
        if cls_[1].startswith('show'):
            idd = cls_[1].split('"')[1]
            ln = f"{cls_[0]} {idd}"
            self.do_show(ln)
            return
        if cls_[1] == 'all()':
            all_objects = storage.all()
            out_len = len(all_objects)
            count = 0
            print("[", end="")
            for k, v in all_objects.items():
                class_part = k.split('.')[0]
                if class_part == cls_[0]:
                    if count == 0:
                        print(v, end="")
                    else:
                        print(", ", end="")
                        print(v, end="")
                    count += 1
            print("]")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()



########################################################################################################
########################################################################################################
########################################################################################################
def default(self, line):
        """default method"""

        cls_ = line.split('.')
        if cls_[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if cls_[1] == 'count()':
            count = 0
            for k, v in storage._FileStorage__objects.items():
                clas_part = k.split('.')[0]
                if clas_part == cls_[0]:
                    count += 1
            print(count)
            return
        if cls_[1].startswith('destroy'):
            idd = cls_[1].split('"')[1]
            ln = f"{cls_[0]} {idd}"
            self.do_destroy(ln)
            return
        if cls_[1].startswith('update') and not cls_[1].endswith('})'):
            idd = cls_[1].split('"')[1]
            att = cls_[1].split('"')[3]
            val = cls_[1].split('"')[5]
            ln = f"{cls_[0]} {idd} {att} \"{val}\""
            self.do_update(ln)
            return
        if cls_[1].startswith('show'):
            idd = cls_[1].split('"')[1]
            ln = f"{cls_[0]} {idd}"
            self.do_show(ln)
            return
        if cls_[1] == 'all()':
            all_objects = storage.all()
            out_len = len(all_objects)
            count = 0
            print("[", end="")
            for k, v in all_objects.items():
                class_part = k.split('.')[0]
                if class_part == cls_[0]:
                    if count == 0:
                        print(v, end="")
                    else:
                        print(", ", end="")
                        print(v, end="")
                    count += 1
            print("]")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()


   
def default(self, line):
        """default method"""

        cls_ = line.split('.')
        if cls_[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if cls_[1] == 'count()':
            count = 0
            for k, v in storage._FileStorage__objects.items():
                clas_part = k.split('.')[0]
                if clas_part == cls_[0]:
                    count += 1
            print(count)
            return
        if cls_[1].startswith('destroy'):
            idd = cls_[1].split('"')[1]
            ln = f"{cls_[0]} {idd}"
            self.do_destroy(ln)
            return
        if cls_[1].startswith('update') and not cls_[1].endswith('})'):
            idd = cls_[1].split('"')[1]
            att = cls_[1].split('"')[3]
            val = cls_[1].split('"')[5]
            ln = f"{cls_[0]} {idd} {att} \"{val}\""
            self.do_update(ln)
            return
        if cls_[1].startswith('show'):
            idd = cls_[1].split('"')[1]
            ln = f"{cls_[0]} {idd}"
            self.do_show(ln)
            return
        if cls_[1] == 'all()':
            all_objects = storage.all()
            out_len = len(all_objects)
            count = 0
            print("[", end="")
            for k, v in all_objects.items():
                class_part = k.split('.')[0]
                if class_part == cls_[0]:
                    if count == 0:
                        print(v, end="")
                    else:
                        print(", ", end="")
                        print(v, end="")
                    count += 1
            print("]")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
