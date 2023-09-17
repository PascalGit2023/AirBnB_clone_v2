#!/usr/bin/python3
""" initialize the filestorage class to always
create an instance of its class that will be
throughout the application """
from os import getenv
from models.engine.file_storage import FileStorage
from models import *
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel, Base

if getenv('HBNB_TYPE_STORAGE') == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
