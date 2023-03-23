#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
