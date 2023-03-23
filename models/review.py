#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
import os
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float

class Review(BaseModel, Base):
    """ Review classto store review information """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename___= "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    else:   
        place_id = ""
        user_id = ""
        text = ""
