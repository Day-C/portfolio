#!/usr/bin/python3
"""init file"""
from models.storage_sys.file_storage import FileStorage


storage = FileStorage()
storage.reload()
