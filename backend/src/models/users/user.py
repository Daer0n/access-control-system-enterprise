from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base

from models.right import Right

class User(Base):
    __tablename__ = 'User'
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    rights = relationship('Right', backref='User', uselist=True)

    