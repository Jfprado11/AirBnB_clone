#!/usr/bin/python3
"""importaing a file module
for creating a instance of the class FileStorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
