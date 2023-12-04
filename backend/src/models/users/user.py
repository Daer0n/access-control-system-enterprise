from sqlalchemy import Column, Integer, String

from database.database import Base

class User(Base):
    __tablename__ = 'User'
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

