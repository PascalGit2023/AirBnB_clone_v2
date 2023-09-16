#!/usr/bin/python3
""" initialize the filestorage class to always
create an instance of its class that will be
throughout the application """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
