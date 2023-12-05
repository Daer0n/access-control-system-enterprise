from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.users.user import User
from database.database import Base

class ObjectFileDirectory(Base):
    __tablename__ = 'ObjectFileDirectory'
    __abstract__ = True
    
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)

    def delete(f_id: int, user: User) -> None:
        pass

    def rename(f_id: int, user: User) -> str:
        pass

    def move(f_id: int, user: User) -> str:
        pass

    def update_f_id(f_id: int, user: User) -> None:
        pass