import os

from typing import Annotated, Any, AsyncGenerator, Callable, Optional

from fastapi import APIRouter, Depends, UploadFile, File
from pydantic import BaseModel

from repositories.fileObjectRepositore import GetFileObjectRepositoreFilter, PatchFileObjectRepositoreFilter
from services.fileObjectService import FileObjectService
from schemas.schemas import FileCreate, FolderCreate
from shared.shared import FolderTypeAccess


SECRET_KEY = os.environ["SECRET_AUTH"]
ALGORITHM = os.environ["AUTH_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["AUTH_ACCESS_TOKEN_EXPIRE_MINUTES"])


def create_router(
    get_service: Callable[[], AsyncGenerator[FileObjectService, Any]],
) -> APIRouter:
    router = APIRouter()

    @router.post(
        "/file/{name}/{path}/{folder_id}/",
        name="Add file",
    )
    async def add_file(
        name: str, 
        path: str, 
        folder_id: int,
        access_type: FolderTypeAccess,
        body: UploadFile = File(...),
        service: FileObjectService = Depends(get_service),
    ):
        file_content = await body.read() 
        dto = FileCreate(
            name=name,
            path=path,
            body=file_content,
            access_type=access_type,
            folder_id=folder_id
        )
        return await service.save_file(dto)
    
    @router.delete(
        "/file/{id}/",
        name="Delete file",
    )
    async def delete_file(
        id: int,
        name: Optional[str] = None,
        service: FileObjectService = Depends(get_service),
    ):
        filter = GetFileObjectRepositoreFilter(
            id=id,
            name=name
        )
        return await service.delete_file(filter)
    
    @router.get(
        "/file/{id}/",
        name="Get file",
    )
    async def read_file(
        id: int,
        name: Optional[str] = None,
        service: FileObjectService = Depends(get_service),
    ):
        filter = GetFileObjectRepositoreFilter(
            id=id,
            name=name
        )
        return await service.read_file(filter)

    @router.patch(
        "/file/{id}/",
        name="Patch file",
    )
    async def update_file(
        id: int, 
        name: Optional[str] = None,
        path: Optional[str] = None,
        service: FileObjectService = Depends(get_service),
    ):
        filter = PatchFileObjectRepositoreFilter(
            id=id, 
            name=name,
            path=path,
        )
        return await service.update_file(filter)

    @router.post(
        "/folder/{name}/{path}/",
        name="Add folder",
    )
    async def add_folder(
        name: str, 
        path: str, 
        service: FileObjectService = Depends(get_service),
    ):
        dto = FolderCreate(
            name = name,
            path = path
        )
        return await service.save_folder(dto)
    
    @router.delete(
        "/folder/{id}/",
        name="Delete folder",
    )
    async def delete_folder(
        id: int,
        name: Optional[str] = None,
        service: FileObjectService = Depends(get_service),
    ):
        filter = GetFileObjectRepositoreFilter(
            id=id,
            name=name
        )
        return await service.delete_folder(filter)
    
    @router.get(
        "/folder/{id}/",
        name="Get folder",
    )
    async def read_folder(
        id: int,
        name: Optional[str] = None,
        service: FileObjectService = Depends(get_service),
    ):
        filter = GetFileObjectRepositoreFilter(
            id=id,
            name=name
        )
        return await service.read_folder(filter)

    @router.patch(
        "/folder/{id}/",
        name="Patch folder",
    )
    async def update_folder(
        id: int, 
        name: Optional[str] = None,
        path: Optional[str] = None,
        service: FileObjectService = Depends(get_service),
    ):
        filter = PatchFileObjectRepositoreFilter(
            id=id, 
            name=name,
            path=path,
        )
        return await service.update_folder(filter)

    return router