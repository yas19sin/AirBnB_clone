#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Module for File Review"""
    place_id = ""
    user_id = ""
    text = ""


"""
    def __init__(self, place_id, user_id):
        Review.place_id = place_id
        Review.user_id = user_id
"""
