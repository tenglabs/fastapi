from pydantic import BaseModel
import datetime


class User(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    password: str


class ShowUser(BaseModel):
    username: str
    email: str
    register_date: datetime.date
    id: int

    class Config:
        orm_mode = True

