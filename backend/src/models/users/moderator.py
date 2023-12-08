from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declared_attr, relationship

from database.database import Base
from models.users.user import User
from schemas.dtos import SaveUserDto

class Moderator(User):
    __tablename__ = 'Moderator'

    role = Column(String, default='Moderator')
    
    @staticmethod
    def from_dto(dto: SaveUserDto) -> 'Moderator':
        return Moderator(
            name = dto.name,
            email = dto.email,
            role = dto.role 
        )