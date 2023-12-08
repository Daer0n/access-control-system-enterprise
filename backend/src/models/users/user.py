from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

from database.database import Base


class User(Base):
    __tablename__ = 'User'
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
