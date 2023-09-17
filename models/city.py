#!/usr/bin/python3
"""  class City that inherits from BaseModel:"""
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import *


class City(BaseModel, Base):
    """state_id: string - empty string
    it will be the State.id
    name: string - empty string"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
