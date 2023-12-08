
from sqlalchemy import Column, Integer, LargeBinary, ForeignKey, Enum
from sqlalchemy.ext.declarative import declared_attr

from database.database import Base

from shared.shared import FolderTypeAccess

from models.objectFileDirectory.folder import Folder
from models.objectFileDirectory.objectFileDirectory import ObjectFileDirectory
from schemas.dtos import SaveFileDto

class File(ObjectFileDirectory):
    __tablename__ = 'File'

    body = Column(LargeBinary, nullable=False)
    access_type = Column(Enum(FolderTypeAccess))

    @declared_attr
    def folder_id(cls):
        return Column(Integer, ForeignKey(Folder.id))

    @staticmethod
    def from_dto(dto: SaveFileDto) -> 'File':
        return File(
            name = dto.name,
            path = dto.path,
            body = dto.body,
            folder_id = dto.folder_id
        )