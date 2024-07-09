#!/usr/bin/python3
"""test database storage system"""
from models.base_model import Base_M
from models.user import User


usr = User()
usr.save

