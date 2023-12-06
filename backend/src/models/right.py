from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, ARRAY, Enum
from sqlalchemy.orm import relationship

from database.database import Base
from models.objectFileDirectory.folder import Folder
from shared.shared import FolderAccessType
from schemas.dtos import SaveRightDto

class Right(Base):
    __tablename__ = 'Right'

    id = Column(Integer, primary_key=True, autoincrement=True)
    folder_id = Column(Integer, ForeignKey(Folder.id))
    rights = Column(Enum(FolderAccessType))

    @staticmethod
    def from_dto(dto: SaveRightDto) -> 'Right':
        return Right(
            folder_id = dto.folder_id,
            rights = dto.rights
        )