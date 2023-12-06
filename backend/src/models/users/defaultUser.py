from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declared_attr

from database.database import Base
from models.users.user import User
from schemas.dtos import SaveUserDto

class DefaultUser(User, Base):
    __tablename__ = 'DefaultUser'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, default='Default user')

    @staticmethod
    def from_dto(dto: SaveUserDto) -> 'DefaultUser':
        return DefaultUser(
            name = dto.name,
            email = dto.email,
            role = dto.role
        )
    