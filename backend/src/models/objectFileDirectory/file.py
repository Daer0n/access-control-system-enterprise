
from sqlalchemy import Column, Integer, LargeBinary, ForeignKey

from database.database import Base

from models.objectFileDirectory.folder import Folder
from models.objectFileDirectory.objectFileDirectory import ObjectFileDirectory
from schemas.dtos import SaveFileDto

class File(ObjectFileDirectory, Base):
    __tablename__ = 'File'

    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(LargeBinary, nullable=False)
    folder_id = Column(Integer, ForeignKey(Folder.id))

    @staticmethod
    def from_dto(dto: SaveFileDto) -> 'File':
        return File(
            name = dto.name,
            path = dto.path,
            body = dto.body,
            folder_id = dto.folder_id
        )