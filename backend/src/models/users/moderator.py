from sqlalchemy import Column, Integer, String

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