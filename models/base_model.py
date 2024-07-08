#!/usr/bin/python3
"""Mother model."""
from datetime import datetime
import uuid
from models import storage


class Base_M():
    """Create and initialive basic methods and attributes of all models."""

    fomat = "%Y-%m-%dT%H:%M:%S:%f"

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes."""

        if kwargs:
            for key in kwargs.keys():
                print("______*****_____")
                if key != '__class__':
                    setattr(self, key, kwargs[key])
            #convert time attribute to correct type
            if type(self.created_at) == str:
                self.created_at = datetime.strptime(self.created_at, self.fomat)
            if type(self.updated_at) == str:
                self.updated_at = datetime.strptime(self.updated_at, self.fomat)
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            self.id = uuid.uuid4()


    def __str__(self):
        """display a sting represnetation of an instance."""

        return f"[{self.__class__.__name__}]({self.id}) ({self.__dict__})"

    def to_dict(self):
        """Convet objects instance to a dictionary."""

        new_dict = self.__dict__
        new_dict['created_at'] = self.created_at.strftime(self.fomat)
        new_dict['updated_at'] = self.updated_at.strftime(self.fomat)
        #add a class key with class name as value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def save(self):
        """save and instance to a storgae system."""

        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()
        
