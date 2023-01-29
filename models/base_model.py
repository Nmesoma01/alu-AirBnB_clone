#!/usr/bin/python3
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

