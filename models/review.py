#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
import os
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float

class Review(BaseModel, Base):
    """ Review classto store review information """ 
    place_id = ""
    user_id = ""
    text = ""
