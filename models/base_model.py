#!/usr/bin/python3
<<<<<<< HEAD
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id, created_at, updated_at):
    self.id = id
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        self.__dict__ =  
    # code

=======
""" a class BaseModel that defines all common attributes/methods for other classes """
>>>>>>> 4777734782456f25fb132c1a9a89859143f6d7e6
