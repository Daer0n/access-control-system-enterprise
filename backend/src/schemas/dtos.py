from pydantic import BaseModel
from typing import List

from shared.shared import FolderTypeAccess

class SaveUserDto(BaseModel):
    name: str
    email: str
    role: str

class SaveRightDto(BaseModel):
    folder_id: int
    rights:  FolderTypeAccess

class SaveFileDto(BaseModel):
    name: str
    path: str
    body: bytes
    folder_id: int

class SaveFolderDto(BaseModel):
    name: str
    path: str
    files: List[SaveFileDto]