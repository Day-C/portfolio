#!/usr/bin/python3
"""Database storage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


models = {}

class DbStorage():
    """Handle storage fo objecst into a mysql database."""

    __engine = ""
    __session = ""

    def __init__(self):
        """collect DB connection parameters from 
        env-variable and connect to a database.
        """

        urs = PHPLS_USER
        pwd = PHPLS_PWD
        hst = "localhost"
        dbs = PHPLS_DB

        db_url = f"mysql+mysqldb://{usr}:{pwd}@{hst}/{dbs}"

        self.__engine = create_engine(db_url, pool_per_oing=True)

    def all(self, cls=None):
        """gets all objects fron the database."""

        all_objs = {}
        if cls != None and cls in models:
            all_objs = self.session.query(models[cls]).all()
        else:
            for key in models.keys():
                all_objs = self.__session.query(models[key]).all()
        return all_objs

    def new(self, obj):
        """Add an onject to the curent session."""

        self.__session.add(obj)

    def save(self):
        """commit changes made on current session to database."""

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
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False_)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        
        self.__session.remove()
