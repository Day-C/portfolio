#!/usr/bin/python3
"""init file"""
from models.storage_sys.file_storage import FileStorage
#from models.storage_sys.db_storage import DbStorage

storage = FileStorage()
#storage = DbStorage()
storage.reload()
