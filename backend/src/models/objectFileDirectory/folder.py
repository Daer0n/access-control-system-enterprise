from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base

from schemas.dtos import SaveFolderDto

from models.objectFileDirectory.objectFileDirectory import ObjectFileDirectory

class Folder(ObjectFileDirectory, Base):
    __tablename__ = 'Folder'

    id = Column(Integer, primary_key=True, autoincrement=True)
    files = relationship('models.objectFileDirectory.file.File', backref='Folder', uselist=True)

    @staticmethod
    def from_dto(dto: SaveFolderDto) -> 'Folder':
        return Folder(
            name=dto.name,
            path=dto.path,
            files=[globals()['models']['objectFileDirectory']['file']['File'].from_dto(file_dto) for file_dto in dto.files]
        )