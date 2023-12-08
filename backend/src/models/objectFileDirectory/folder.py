from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

from database.database import Base

from schemas.dtos import SaveFolderDto

from models.objectFileDirectory.objectFileDirectory import ObjectFileDirectory

class Folder(ObjectFileDirectory):
    __tablename__ = 'Folder'


    @declared_attr
    def files(cls):
        return relationship('File', backref='Folder', uselist=True)

    @staticmethod
    def from_dto(dto: SaveFolderDto) -> 'Folder':
        from models.objectFileDirectory.file import File
        return Folder(
            name=dto.name,
            path=dto.path,
            files=[File.from_dto(file_dto) for file_dto in dto.files]
        )