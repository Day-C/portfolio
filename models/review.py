#!/usr/bin/python3
"""Reviews class/"""
from models/base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class Review(BaseModel, Base):
    """Define revires object attributes."""

    #if getenv("PHPSL_STORAGE_T") == "db":
    __tablename__ = "Reviews"
    
    user_id = Column("user_id", String(60), ForeignKey("Users.id"))
    drug_id = Column("drug_id", String(60), ForeignKey("Drugs.id"))
    text = Column("text", String(1024), nullable=False)

    user_id = ""
    drug_id = ""
    text = ""
