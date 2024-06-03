""" Schemas
"""
import logging
from pydantic import BaseModel


logger = logging.getLogger("schemas")

def Config(BaseModel):
    id: int

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int
    username: str | None = None
    hashed_password: str | None = None
    is_active: bool | None = None
    items: list[Item] = []

    class Config:
        from_attributes = True
    #username: str | None = None
    #email: str | None = None
    #full_name: str | None = None
    #disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None