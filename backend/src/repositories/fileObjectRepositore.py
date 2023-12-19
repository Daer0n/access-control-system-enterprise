from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, select
from fastapi import HTTPException

from dataclasses import dataclass
from pydantic import BaseModel
from typing import Union

from models.objectFileDirectory.file import File
from models.objectFileDirectory.folder import Folder
from shared.shared import FolderTypeAccess

@dataclass(frozen=True)
class GetFileObjectRepositoreFilter:
    id: int | None = None
    name: str | None = None

@dataclass(frozen=True)
class PatchFileObjectRepositoreFilter:
    id: int
    name: str | None = None
    path: str | None = None

@dataclass(frozen=True)
class PatchFileRightsFilter:
    id: int
    access_type: FolderTypeAccess
    name: str | None = None

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

    async def save_file(self, file: File):
        async with self.session.begin_nested():
            self.session.add(file)
            await self.session.flush()
        await self.session.commit()
        return file

    async def save_folder(self, folder: Folder):
        async with self.session.begin_nested():
            self.session.add(folder)
            await self.session.flush()
        await self.session.commit()
        return folder

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
        return await self.save_file(file)

    async def update_folder(self, filter: PatchFileObjectRepositoreFilter):
        folder = await self._get_object_by_id(filter.id, "folder")
        if filter.name is not None:
            folder.name = filter.name
        if filter.path is not None:
            folder.path = filter.path
        return await self.save_folder(folder)
    
    async def change_file_rights(self, filter: PatchFileRightsFilter):
        file = await self._get_object_by_id(filter.id, "file")
        if file is not None:
            file.access_type = filter.access_type
        return await self.save_file(file)
    
    async def read_all_folders(self) -> list[Folder]:
        stmt = select(Folder)
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Folders not found")
        return items 
    
    async def read_all_files_from_folders(self, folder_id: int):
        stmt = select(File).where(File.folder_id == folder_id)
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Files not found")
        return items 
        


