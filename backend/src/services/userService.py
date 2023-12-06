from __future__ import annotations

from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncEngine

from sqlalchemy.ext.asyncio.session import AsyncSession
from repositories.userRepositories.user import UserRepository
from schemas.dtos import SaveUserDto
from models.users.administrator import Administrator

from repositories.userRepositories import save_administator

class UserService:
    def __init__(self, database: UserRepository):
        self._database = database

    @staticmethod
    @asynccontextmanager
    async def from_engine(engine: AsyncEngine):
        async with AsyncSession(engine) as session:
            async with session.begin():
                yield UserService.from_session(session)

    @staticmethod
    def from_session(session: AsyncSession) -> UserService:
        database = UserRepository(session)
        return UserService(database)
    
    async def save_administrator(self, dto: SaveUserDto):
        model = Administrator.from_dto(dto)
        return await self._database.save_administrator(model)

    
