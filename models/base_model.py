#!/usr/bin/python3
""" base model super class to be used
by allsub classes """

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Basmodel for other classes save __str__ new """

    def __init__(self, *args, **kwargs):
        """ initializes the class attributes*arg is an unused variable"""
        str_fdate = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        # self.created_at = datetime.today()
        # self.updated_at = datetime.today()
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at":
                    self.__dict__[k] = datetime.strptime(v, str_fdate)
                elif k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, str_fdate)
                if k != "__class__":
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            # models.storage.new(self)

    def __str__(self):
        """ string representation of the BaseModel intance """
        # clName = self.__class__.__name__
        clName = type(self).__name__
        str = f"[{clName}] ({self.id}) {self.__dict__}"
        return str

    def save(self):
        """ updates the instance attribute update_at """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """return all keys and values of the objectinstance from __dict__"""
        dictcopy = self.__dict__.copy()
        if type(self.created_at) is str:
            pass
            # dictcopy["created_at"] = self.created_at
        else:
            dictcopy["created_at"] = self.created_at.isoformat()
        if type(self.updated_at) is str:
            pass
            # dictcopy["updated_at"] = self.updated_at
        else:
            dictcopy["updated_at"] = self.updated_at.isoformat()
        dictcopy["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in dictcopy.keys():
            del dictcopy['_sa_instance_state']
        return dictcopy
