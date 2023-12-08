from sqlalchemy import Column, Integer, String

from database.database import Base

class ObjectFileDirectory(Base):
    __tablename__ = 'ObjectFileDirectory'
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
