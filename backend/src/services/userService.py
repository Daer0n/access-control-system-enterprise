from __future__ import annotations
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from repositories.userRepository import UserRepository, GetUserFilter, PatchUserFilter

from schemas.dtos import SaveUserDto
from models.users.administrator import Administrator
from models.users.moderator import Moderator
from models.users.defaultUser import DefaultUser

class UserService():
    def __init__(self, db: AsyncSession):
        self._database = UserRepository(db) 

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
        model = Administrator(
            name=dto.name,
            email=dto.email,
            role=dto.role,
            hashed_password=dto.password
        )
        return await self._database.save_administrator(model)
    
    async def save_moderator(self, dto: SaveUserDto):
        model = Moderator(
            name=dto.name,
            email=dto.email,
            role=dto.role,
            hashed_password=dto.password
        )
        return await self._database.save_moderator(model)
    
    async def save_default_user(self, dto: SaveUserDto):
        model = DefaultUser(
            name=dto.name,
            email=dto.email,
            role=dto.role,
            hashed_password=dto.password
        )
        return await self._database.save_default_user(model)
    
    async def delete_administrator(self, filter: GetUserFilter):
        return await self._database.delete_administrator(filter)
    
    async def delete_moderator(self, filter: GetUserFilter):
        return await self._database.delete_moderator(filter)

    async def delete_default_user(self, filter: GetUserFilter):
        return await self._database.delete_default_user(filter)

    async def read_administator(self, filter: GetUserFilter):
        return await self._database.read_administrator(filter)
    
    async def read_moderator(self, filter: GetUserFilter):
        return await self._database.read_moderator(filter)
    
    async def read_default_user(self, filter: GetUserFilter):
        return await self._database.read_default_user(filter)
    
    async def update_administrator(self, filter: PatchUserFilter):
        return await self._database.update_administrator(filter)
    
    async def update_moderator(self, filter: PatchUserFilter):
        return await self._database.update_moderator(filter)
    
    async def update_default_user(self, filter: PatchUserFilter):
        return await self._database.update_default_user(filter)
    
    async def change_user_role(self, filter: GetUserFilter):
        return await self._database.change_user_role(filter)
    
    async def change_moderator_role(self, filter: GetUserFilter):
        return await self._database.change_moderator_role(filter)
    
    async def read_all_administrators(self):
        return await self._database.read_all_administrators()
    
    async def read_all_moderators(self):
        return await self._database.read_all_moderators()
    
    async def read_all_default_users(self):
        return await self._database.read_all_default_users()
    
    

