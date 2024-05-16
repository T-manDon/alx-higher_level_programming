#!/usr/bin/python3
""" the script gives a state model containing class definition
 of state and theinstance Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City
Base = declarative_base()


class State(Base):
    """ script inherits Base Tips
    links to MySQL table states
    attribute id represents the column
     of the auto-generated integers, cannot
      be null and comprises primary key
    class attribute represents the column
     of a string with 128 characters
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
