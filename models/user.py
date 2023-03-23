#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
import models.place     
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import sqlalchemy.orm   


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "users"
        # Colonnes
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='all, delete', backref="user")
        reviews = relationship('Review', cascade='all, delete', backref="user")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
