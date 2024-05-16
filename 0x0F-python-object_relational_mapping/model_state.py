#!/usr/bin/python3
"""
Gives state model containing class definition
 of the States and Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    takes over from the Base
    joins to MySQL table states
    class attributes id represnting column
     of the auto-generated, peculiar integer, can't
      be null or empty
    class vattributes name representing the col
     of a stri characters and
      can't be normull

    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
