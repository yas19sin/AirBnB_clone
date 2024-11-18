#!/usr/bin/python3
"""Module for File User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Module for File User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
