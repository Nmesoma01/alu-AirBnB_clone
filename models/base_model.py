#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *arg, **kw):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self, *arg, **kw):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self, *arg, **kw):
        self.updated_at = datetime.now()

    def __dict__(self, *arg, **kw):
        dic = {}
        dic = dict(self.__dict__)
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
