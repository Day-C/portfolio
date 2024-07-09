#!/usr/bin/python3
"""contain user class """
from models.base_model import Base, Base_M
from sqlalchemy import Column, String, Integer

class User(Base_M, Base):
    """Define structure of user object."""

    #if getenv('PHPSL_STORAGE_T') == "db":
    __tablename__ = "Users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    
    #else:
    first_name = ""
    last_name = ""
    email = ""
    password = ""
