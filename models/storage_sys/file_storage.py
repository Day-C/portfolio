#!/usr/bin/python3
"""file storage system"""
import json


class FileStorage():
    """Handle all the methods and fr storing data into a file system."""

    __filename = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return all objects."""

        if cls:
            new_dict = {}
            all_objs = self.reload()
            for key in all_objs.keys:
                spltKey = key.split('.')
                if spltKey[0] == cls.__name__:
                    new_dict[key] = all_objs[key]
            return new_dict
        if self.reload():
            return self.reload()
        return {}
    def new(self, obj):
        """Create  a dictionary with object values"""

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.__dict__

    def save(self):
        """Save a new object into file."""
        objs = self.all()
        for key in self.__objects.keys():
            objs[key] = self.__objects
        with open(self.__filename, "w") as f:
            f.write(json.dumps(objs, default=str))

    def reload(self):
        """READ all the objes in the storage."""

        try:
            with open(self.__filename, 'r') as f:
                data = f.read()
                return json.loads(data)
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """Remove a specific object from storage."""

        if obj:
            objName = obj.__class__.__name__
            all_objs = self.all(objName)
            for key in all_objs.keys():
                spltKey = key.split('.')
                if spltkey[1] == obj['id']:
                    del all_objs[key]
                    break
            with open(self.__filename, 'w') as f:
                f.write(json.dumps(all_objs, default=str))
