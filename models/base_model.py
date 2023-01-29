#!/usr/bin/python3
""" a class BaseModel that defines all common attributes/methods for other classes """

from datetime import datetime
import models
import uuid
from uuid import uuid4


class BaseModel:
    """Initializing class BaseModel"""


def __init__(self, *args, **kwargs):

 self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

def save(self):
    """updates the public instance attribute updated_at with the current datetime"""
     self.updated_at = datetime.today()
        models.storage.save()

def to_dict(self):
    """returns a dictionary containing all keys/values of __dict__ of the instance"""
    rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

def __str__(self):
    """should print: [<class name>] (<self.id>) <self.__dict__>"""
    clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
