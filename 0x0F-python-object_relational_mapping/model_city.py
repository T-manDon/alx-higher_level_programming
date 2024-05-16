#!/usr/bin/python3
"""This script gives the state model with class definition
 of city and the instance Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    inherits from the links to the MySQL city table

    class attribute id representing the column of
    an auto-generated, unique y

    class attribute representing the columns
    of a string of 128 be null

    class has state_id representing column
    of integer, and has a unique key to states.id

    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
