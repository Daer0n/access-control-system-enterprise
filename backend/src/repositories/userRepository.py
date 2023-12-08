from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, select

from fastapi import HTTPException

from pydantic import BaseModel

from typing import Union

from models.users.moderator import Moderator
from models.users.administrator import Administrator
from models.users.defaultUser import DefaultUser


class GetUserFilter(BaseModel):
    id: int | None = None
    name: str | None = None

class PatchUserFilter(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None

class UserRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_user_by_id(self, id: int, user_type: str) -> Union[Administrator, Moderator, DefaultUser]:
        if user_type == "administrator":
            stmt = select(Administrator).where(Administrator.id == id)
            return await self.session.scalar(stmt)
        elif user_type == "moderator":
            stmt = select(Moderator).where(Moderator.id == id)
            return await self.session.scalar(stmt)
        elif user_type == "user":
            stmt = select(DefaultUser).where(DefaultUser.id == id)
            return await self.session.scalar(stmt)
        else:
            raise ValueError("Invalid user_type specified.")

    async def save_administrator(self, model: Administrator):
        async with self.session.begin():
            stmt = insert(Administrator).values(**model.dict())
            await self.session.execute(stmt)
            await self.session.commit()

    async def save_moderator(self, model: Moderator):
        async with self.session.begin():
            stmt = insert(Moderator).values(**model.dict())
            await self.session.execute(stmt)
            await self.session.commit()

    async def save_default_user(self, model: DefaultUser):
        async with self.session.begin():
            stmt = insert(DefaultUser).values(**model.dict())
            await self.session.execute(stmt)
            await self.session.commit()

    async def delete_administrator(self, filter: GetUserFilter):
        models = await self.read_administrator(filter)
        for model in models:
            await self.session.delete(model)
        await self.session.commit()
        return {'ok': True}
    
    async def delete_moderator(self, filter: GetUserFilter):
        models = await self.read_moderator(filter)
        for model in models:
            await self.session.delete(model)
        await self.session.commit()
        return {'ok': True}
    
    async def delete_default_user(self, filter: GetUserFilter):
        models = await self.read_default_user(filter)
        for model in models:
            await self.session.delete(model)
        await self.session.commit()
        return {'ok': True}

    async def read_administrator(self, filter: GetUserFilter) -> list[Administrator]:
        stmt = select(Administrator).order_by(Administrator.id, Administrator.name)
        if filter.id is not None:
            stmt = stmt.where(Administrator.id == filter.id)
        if filter.name is not None:
            stmt = stmt.where(Administrator.name.ilike(filter.name))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Administrator not found")
        return items 

    async def read_moderator(self, filter: GetUserFilter) -> list[Moderator]:
        stmt = select(Moderator).order_by(Moderator.id, Moderator.name)
        if filter.id is not None:
            stmt = stmt.where(Moderator.id == filter.id)
        if filter.name is not None:
            stmt = stmt.where(Moderator.name.ilike(filter.name))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Moderator not found")
        return items 

    async def read_default_user(self, filter: GetUserFilter) -> list[DefaultUser]:
        stmt = select(DefaultUser).order_by(DefaultUser.id, DefaultUser.name)
        if filter.id is not None:
            stmt = stmt.where(DefaultUser.id == filter.id)
        if filter.name is not None:
            stmt = stmt.where(DefaultUser.name.ilike(filter.name))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="User not found")
        return items 
    
    async def update_administrator(self, filter: PatchUserFilter):
        administrator = await self._get_user_by_id(filter.id, "administrator")
        if filter.name is not None:
            administrator.name = filter.name
        if filter.email is not None:
            administrator.email = filter.email
        return self.save_administrator(administrator)
    
    async def update_moderator(self, filter: PatchUserFilter):
        moderator = await self._get_user_by_id(filter.id, "moderator")
        if filter.name is not None:
            moderator.name = filter.name
        if filter.email is not None:
            moderator.email = filter.email
        return self.save_moderator(moderator)
    
    async def update_default_user(self, filter: PatchUserFilter):
        user = await self._get_user_by_id(filter.id, "user")
        if filter.name is not None:
            user.name = filter.name
        if filter.email is not None:
            user.email = filter.email
        return self.save_default_user(user)


    def change_body() -> LargeBinary:
        pass

    def delete() -> None:
        pass