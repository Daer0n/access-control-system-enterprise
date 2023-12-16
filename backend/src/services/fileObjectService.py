from __future__ import annotations
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from models.objectFileDirectory.file import File
from models.objectFileDirectory.folder import Folder

from schemas.dtos import SaveFileDto, SaveFolderDto

from repositories.fileObjectRepositore import FileObjectRepostitore, GetFileObjectRepositoreFilter, PatchFileRightsFilter

class FileObjectService:
    def __init__(self, db: AsyncSession):
        self._database = FileObjectRepostitore(db) 

    @staticmethod
    @asynccontextmanager
    async def from_engine(engine: AsyncEngine):
        async with AsyncSession(engine) as session:
            async with session.begin():
                yield FileObjectService.from_session(session)

    @staticmethod
    def from_session(session: AsyncSession) -> FileObjectService:
        database = FileObjectRepostitore(session)
        return FileObjectService(database)
    
    async def save_file(self, dto: SaveFileDto):
        model = File(
            name = dto.name,
            path = dto.path,
            body = dto.body,
            folder_id = dto.folder_id,
            access_type=dto.access_type
        )
        return await self._database.save_file(model)
    
    async def save_folder(self, dto: SaveFolderDto):
        model = Folder(
            name = dto.name,
            path = dto.path
        )
        return await self._database.save_folder(model)
    
    async def delete_file(self, filter: GetFileObjectRepositoreFilter):
        return await self._database.delete_file(filter)
    
    async def delete_folder(self, filter: GetFileObjectRepositoreFilter):
        return await self._database.delete_folder(filter)
    
    async def read_file(self, filter: GetFileObjectRepositoreFilter):
        return await self._database.read_file(filter)
    
    async def read_folder(self, filter: GetFileObjectRepositoreFilter):
        return await self._database.read_folder(filter)

    async def update_file(self, filter: GetFileObjectRepositoreFilter):
        return await self._database.update_file(filter)
    
    async def update_folder(self, filter: GetFileObjectRepositoreFilter):
        return await self._database.update_folder(filter)
    
    async def change_file_rights(self, filter: PatchFileRightsFilter):
        return await self._database.change_file_rights(filter)