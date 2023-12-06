from sqlalchemy import Column, Integer, String

from database.database import Base

class ObjectFileDirectory(Base):
    __tablename__ = 'ObjectFileDirectory'
    __abstract__ = True
    
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
