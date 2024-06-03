""" Schemas
"""
import logging
from pydantic import BaseModel


logger = logging.getLogger("schemas")

class Config(BaseModel):
    """
    Config pydantic
    """
    id: int

class ItemBase(BaseModel):
    """
    Config pydantic
    """
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    """
    Config pydantic
    """
    pass


class Item(ItemBase):
    """
    Config pydantic
    """
    id: int
    owner_id: int

    class Config:
        """
        Config pydantic
        """
        from_attributes = True


class UserBase(BaseModel):
    """
    Config pydantic
    """
    email: str


class UserCreate(UserBase):
    """
    Config pydantic
    """
    password: str


class User(BaseModel):
    """
    Config pydantic
    """
    id: int
    username: str | None = None
    is_active: bool | None = None
    items: list[Item] = []

    class Config:
        """
        Config pydantic
        """
        from_attributes = True
    #username: str | None = None
    #email: str | None = None
    #full_name: str | None = None
    #disabled: bool | None = None


class UserInDB(User):
    """
    Config pydantic
    """
    hashed_password: str

class Token(BaseModel):
    """
    Config pydantic
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Config pydantic
    """
    username: str | None = None
