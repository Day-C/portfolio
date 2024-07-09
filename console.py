#!/usr/bin/pythoin3
'''Console for models'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json

class HBNBCommand(cmd.Cmd):
    '''command interpriter to manipulate models.'''

    clss = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
    'Amenity': Amenity, 'Place': Place, 'Review': Review}
    
    def do_help(self, cmd):
        '''display helpful info about the use of the module.'''

        print("hello there want some help?")

    def do_create(self, line):
        '''Create a new instance of a class.'''

        args = line.split( )
        if len(args) != 0:
            if args[0] in self.clss:
                #check for kwargs
                kwargs = self.to_kwargs(str(line))
                # now create the instance
                obj = self.clss[args[0]](**kwargs)
                print(obj.id)
                obj.save()
            else:
                print('*** class does not exist ****')
        else:
            print("**** class name missing ****")


    def to_kwargs(self, key_vals):
        '''Convers string into dictionary.'''

        kwargs = {}
        if  key_vals != None:
            #slpit each assignment
            attr = key_vals.split(' ')
            for item in range(len(attr)):
                if '=' in attr[item]:
                    attr[item] = attr[item].replace('_', ' ')
                    key_val = attr[item].split('=')
                    #check if (") character in value
                    if not '"' in key_val[1]:
                        #check for decimand point and convert to float
                        if '.' in key_val[1]:
                            key_val[1] = float(key_val[1])
                        else:
                        # convert to integer
                            key_val[1] = int(key_val[1])
                    else:
                        key_val[1] = key_val[1].strip('"')
                    kwargs[key_val[0]] =  key_val[1]
            return kwargs
                
    def do_show(self, line):
        '''display representation of instance based on class name and id'''

        if len(line) != 0:
            # Split  line to various arguments
            args = line.split(' ')
            #check for command arguments
            found = 0
            if args[0] in self.clss:
                if len(args) > 1:
                    # Rea all objects in file storage
                    all_objs = models.storage.all()
                    for key in all_objs.keys():
                        # Split each key and compare id's
                        name_id = key.split('.')
                        if name_id[1] == args[1]:
                            print(all_objs[key])
                            found += 1
                    if found == 0:
                        print('**** no instance found for id ****')
                else:
                    print('**** instance id missing ****')
            else:
                print('**** class does not exist ****')
        else:
            print('**** class name missing ****')

    def do_destroy(self, line):
        '''Delelte an object from storage.'''

        if len(line) != 0:
            args = line.split(' ')
            found = 0
            if args[0] in self.clss:
                if len(args) > 1:
                    # Read all objects in file storage
                    all_objs = models.storage.all()
                    for key in all_objs.keys():
                        # Split each key to get id
                        name_id = key.split('.')
                        if name_id[1] == args[1]:
                            del all_objs[key]
                            found += 1
                            break
                    # save edited dictionary
                    with open("file.json", 'w') as f:
                        f.write(json.dumps(all_objs))
                    if found == 0:
                        print('**** no instance found for id ****')
                else:
                    print('**** instance id missing ****')
            else:
                print('**** class does not exist ****')
        else:
            print('**** class name missing ****')

    def do_all(self, line):
        '''Prints all string representation of all instances
        based or not on the class name.'''

        if len(line) > 0:

            arg = line.split(' ')
            if arg[0] in self.clss:
                # Read all data from file storage
                all_objs = models.storage.all()
                clss = []
                for  key in all_objs.keys():
                    # Split all keys to get class name
                    name_id = key.split('.')
                    if name_id[0] == line:
                        # append to clss list
                        clss.append(all_objs[key])
                print(clss)
            else:
                print('**** class does not exists ****')
        else:
            print('**** class name missing ****')

    def do_update(self, line):
        '''Updates an instance based on the class name,
        and id by adding or updating attribute then 
        (save the change into the JSON file)'''

        if len(line) > 0:
            args = line.split(' ')
            if args[0] in self.clss:
                if len(args) > 1:
                    if len(args) > 2:
                        if len(args) > 3:
                            # Read data from file
                            all_objs = models.storage.all()
                            for key in all_objs.keys():
                                name_id = key.split('.')
                                if name_id[1] == args[1]:
                                    obj_attr = all_objs[key]
                                    try:
                                        obj_attr[args[2]] = args[3]
                                    except KeyError:
                                        obj_attr[arg[2]] = args[3]
                                    break
                            # Save the new instance updates
                            with open('file.json', 'w') as f:
                                f.write(json.dumps(all_objs))
                        else:
                            print('**** value missing ****')
                    else:
                        print('**** attribute name missing ****')
                else:
                    print('**** instance id missing ****')
            else:
                print('**** class does not exist ****')
        else:
            print('**** class name missing ****')


    def do_quit(self):
        '''End console'''

        return True

    def EOF(self):
        '''exit the console.'''

        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
