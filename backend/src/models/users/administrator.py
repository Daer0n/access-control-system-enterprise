from __future__ import annotations
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declared_attr, relationship

from database.database import Base
from models.users.user import User
from schemas.dtos import SaveUserDto

class Administrator(User, Base):
    __tablename__ = 'Administrator'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, default='Administrator')

    @staticmethod
    def from_dto(dto: SaveUserDto) -> Administrator:
        return Administrator(
            name=dto.name,
            email=dto.email,
            role=dto.role
        )