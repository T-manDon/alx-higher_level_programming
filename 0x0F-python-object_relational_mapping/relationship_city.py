#!/usr/bin/python3
"""Script that defines state model with class definition
 of the city and the Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ script inherits the imported model_state
    links to MySQL tables

    class attribute id representing the column of
    an auto-generated and unique intimary keymon

    class aligns ame representing the column
    of a string of 128ull

    class attribute state_id representing a column
    of an integer, cannot be null and has foreign key

    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
