#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *arg, **kw):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def save(self, *arg):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
 
