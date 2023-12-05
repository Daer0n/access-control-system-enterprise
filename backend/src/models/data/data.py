from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, ARRAY, Enum
from sqlalchemy.orm import relationship

from database.database import Base
from models.objectFileDirectory.folder import Folder
from shared.shared import FolderAccessType

class Data(Base):
    __tablename__ = 'Data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    folder_id = Column(Integer, ForeignKey(Folder.id))
    rights = Column(Enum(FolderAccessType))