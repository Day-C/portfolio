#!/usr/bin/python3
"""Database storage"""

import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

classes = {}

class DbStorage():
    """Handle storage fo objecst into a mysql database."""

    __engine = None
    __session = None

    def __init__(self):
        """collect DB connection parameters from 
        env-variable and connect to a database.
        """

        usr = 'pharmap_dev'
        pwd = 'pharmapwd'
        hst = 'localhost'
        dbs = 'pharmap_db'

        db_url = f"mysql+mysqldb://{usr}:{pwd}@{hst}/{dbs}"

        self.__engine = create_engine(db_url)

    def all(self, cls=None):
        """gets all objects fron the database."""

        all_objs = {}
        if cls != None and cls in classes:
            all_objs = self.session.query(classes[cls]).all()
        else:
            for key in classes.keys():
                all_objs = self.__session.query(classes[key]).all()
        return all_objs

    def new(self, obj):
        """Add an onject to the curent session."""
        print("adding to session")
        self.__session.add(obj)

    def save(self):
        """commit changes made on current session to database."""
        print("commiting session")
        self.__session.commit()

    def delete(self, obj=None):
        """Remove an object from the current session ."""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables of the database."""

        #create all table
        Base.metadata.create_all(self.__engine)
        #creates a session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        
        self.__session.remove()
