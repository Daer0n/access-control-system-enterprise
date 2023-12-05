
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.users.user import User
from database.database import Base

class Folder(Base):
    __tablename__ = 'Folder'

    id = Column(Integer, primary_key=True, autoincrement=True)
    files = relationship('File', backref='Folder', uselist=True)

    def delete(folder_id: int, user: User) -> None:
        pass
