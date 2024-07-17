#!/usr/bin/env python3
"""  tHE shebang for python"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ the user class"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=True)
    hashed_password = Column(String(250), unique=False, nullable=False)
    session_id = Column(String(250), unique=False, nullable=True)
    reset_token = Column(String(250), unique=True, nullable=True)
