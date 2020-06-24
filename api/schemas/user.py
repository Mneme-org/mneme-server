from typing import List
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from . import Journal


class UserBase(BaseModel):
    encrypted: bool = False
    username: str
    # This is only needed if the instance is private, otherwise there are no admins
    admin: bool = False


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str

    journals: List[Journal] = []

    class Config:
        orm_mode = True


class UserPassword(BaseModel):
    """For updating the user password"""
    current_password: str
    new_password: str
