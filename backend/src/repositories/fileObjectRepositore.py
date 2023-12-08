from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, select

from fastapi import HTTPException

from pydantic import BaseModel

from typing import Union

from models.objectFileDirectory.file import File
from models.objectFileDirectory.folder import Folder


class GetFileObjectRepositoreFilter(BaseModel):
    id: int | None = None
    name: str | None = None

class PatchFileObjectRepositoreFilter(BaseModel):
    id: int
    name: str | None = None
    path: str | None = None

class FileObjectRepostitore:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_object_by_id(self, id: int, user_type: str) -> Union[File, Folder]:
        if user_type == "file":
            stmt = select(File).where(File.id == id)
            return await self.session.scalar(stmt)
        elif user_type == "folder":
            stmt = select(Folder).where(Folder.id == id)
            return await self.session.scalar(stmt)
        else:
            raise ValueError("Invalid object_type specified.")

    async def save_file(self, model: File):
        async with self.session.begin():
            stmt = insert(File).values(**model.dict())
            await self.session.execute(stmt)
            await self.session.commit()

    async def save_folder(self, model: Folder):
        async with self.session.begin():
            stmt = insert(Folder).values(**model.dict())
            await self.session.execute(stmt)
            await self.session.commit()

    async def delete_file(self, filter: GetFileObjectRepositoreFilter):
        models = await self.read_file(filter)
        for model in models:
            await self.session.delete(model)
        await self.session.commit()
        return {'ok': True}
    
    async def delete_folder(self, filter: GetFileObjectRepositoreFilter):
        models = await self.read_folder(filter)
        for model in models:
            await self.session.delete(model)
        await self.session.commit()
        return {'ok': True}

    async def read_file(self, filter: GetFileObjectRepositoreFilter) -> list[File]:
        stmt = select(File).order_by(File.id, File.name)
        if filter.id is not None:
            stmt = stmt.where(File.id == filter.id)
        if filter.name is not None:
            stmt = stmt.where(File.name.ilike(filter.name))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="File not found")
        return items 
    
    async def read_folder(self, filter: GetFileObjectRepositoreFilter) -> list[Folder]:
        stmt = select(Folder).order_by(Folder.id, Folder.name)
        if filter.id is not None:
            stmt = stmt.where(Folder.id == filter.id)
        if filter.name is not None:
            stmt = stmt.where(Folder.name.ilike(filter.name))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Folder not found")
        return items 
    
    async def update_file(self, filter: PatchFileObjectRepositoreFilter):
        file = await self._get_object_by_id(filter.id, "file")
        if filter.name is not None:
            file.name = filter.name
        if filter.path is not None:
            file.path = filter.path
        return self.save_file(file)

    async def update_folder(self, filter: PatchFileObjectRepositoreFilter):
        folder = await self._get_object_by_id(filter.id, "folder")
        if filter.name is not None:
            folder.name = filter.name
        if filter.path is not None:
            folder.path = filter.path
        return self.save_folder(folder)

