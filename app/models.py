import datetime
from sqlalchemy import  Column,  Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    register_date = Column(DateTime, default=datetime.datetime.utcnow)

