
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey

from database.database import Base

from models.folder import Folder

class File(Base):
    __tablename__ = 'File'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    body = Column(LargeBinary, nullable=False)
    folder_id = Column(Integer, ForeignKey(Folder.id))

    def change_body():
        pass

    def delete(file_id):
        pass
