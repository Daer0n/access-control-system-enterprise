
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey

from database.database import Base

from models.objectFileDirectory.folder import Folder
from models.objectFileDirectory.objectFileDirectory import ObjectFileDirectory
from models.users.user import User

class File(ObjectFileDirectory, Base):
    __tablename__ = 'File'

    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(LargeBinary, nullable=False)
    folder_id = Column(Integer, ForeignKey(Folder.id))

    def change_body() -> LargeBinary:
        pass

    def delete(file_id, user: User) -> None:
        pass
