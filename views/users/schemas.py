import json
import uuid

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=32)


def generate_token():
    return str(uuid.uuid4())


class UserOut(UserBase):
    id: int


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)


class UserIn(UserBase):
    pass
