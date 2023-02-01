#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        self.__dict__ =  dict(created_at = self.created_at.isoformat())
        self.__dict__ =  dict(updated_at = self.updated_at.isoformat())
        self.__dict__ =  dict(created_at = self.created_at.isoformat())

