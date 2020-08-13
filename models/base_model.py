#!/usr/bin/python3
"""
BaseModel class file
"""
import sqlalchemy
from datetime import datetime
import uuid
import sqlalchemy
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """BaseModel that defines all common attr/methods for other classes:"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """instance constructor and instance instantiation"""

        t = '%Y-%m-%dT%H:%M:%S.%f'
        if len(kwargs) > 1:
            if 'a' not in kwargs:
                for key, value in kwargs.items():
                    if key != "__class__":
                        if key == "created_at" or key == 'updated_at':
                            setattr(self, key, datetime.strptime(value, t))
                        else:
                            setattr(self, key, value)
            else:
                del kwargs['a']
                for key, value in kwargs.items():
                    setattr(self, key, value)
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """string readable representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """return a dictionnary representation of the class"""
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in d:
            del d["_sa_instance_state"]
        return d

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
