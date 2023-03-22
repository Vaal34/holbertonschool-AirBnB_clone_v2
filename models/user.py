#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, DateTime, String, ForeignKey
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "users"
        email = Column(String(189), nullable=False)
        password = Column(String(189), nullable=False)
        first_name = Column(String(189), nullable=False)
        last_name = Column(String(189), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
