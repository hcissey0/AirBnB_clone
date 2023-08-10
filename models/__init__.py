#!/usr/bin/python3
"""This is the __init__.py file"""

from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
