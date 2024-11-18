#!/usr/bin/python3
"""
Module defining the BaseModel class as the base class for all models.
Handles initialization, serialization, and deserialization of instances.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all models. Defines common attributes and methods.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a new instance of the BaseModel class.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for iKey, value in kwargs.items():
                if iKey in ["created_at", "updated_at"]:
                    self.__dict__[iKey] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif iKey != "__class__":
                    self.__dict__[iKey] = value
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the instance.
        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """
        Updates the public instance updated_at attribute and saves changes.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the instance.
        Returns:
            dict: Dictionary representation of the instance.
        """
        todict = dict(self.__dict__)
        todict["__class__"] = self.__class__.__name__
        if not isinstance(todict["created_at"], str):
            todict["created_at"] = todict["created_at"].isoformat()
        if not isinstance(todict["updated_at"], str):
            todict["updated_at"] = todict["updated_at"].isoformat()
        return todict
