from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel, Field
from shared.shared import FolderTypeAccess


class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    email: str
    role: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    email: str
    role: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class FileCreate(BaseModel):
    name: str
    path: str
    body: bytes = Field(..., description="Binary data of the file")
    folder_id: int
    access_type: FolderTypeAccess

class FolderCreate(BaseModel):
    name: str
    path: str
