#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or Database depending of the variable storage_type"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

import os
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = FileStorage() #storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
