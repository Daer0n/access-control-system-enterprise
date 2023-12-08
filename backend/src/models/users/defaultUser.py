from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declared_attr

from database.database import Base
from models.users.user import User
from schemas.dtos import SaveUserDto

class DefaultUser(User):
    __tablename__ = 'DefaultUser'

    role = Column(String, default='DefaultUser')


    @staticmethod
    def from_dto(dto: SaveUserDto) -> 'DefaultUser':
        return DefaultUser(
            name = dto.name,
            email = dto.email,
            role = dto.role
        )
    