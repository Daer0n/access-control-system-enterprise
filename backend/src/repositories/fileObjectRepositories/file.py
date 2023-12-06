from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import LargeBinary

from pydantic import BaseModel

from models.users.user import User
from repositories.fileObjectRepositories.fileObjectRepositore import FileObjectRepostitore

class GetFileFilter(BaseModel):
    id: int | None = None
    file_name: str | None = None

class FileRepository(FileObjectRepostitore):
    def __init__(self, session: AsyncSession):
        self.session = session

    def change_body() -> LargeBinary:
        pass

    def delete() -> None:
        pass

    #def create(Models) -> None
    #def get(GetFileFilter) -> Models

#+ create(object: ObjectFileDirectory, data: Dict[str,str]): None
#+ read(object: ObjectFileDirectory, data: Dict[str,str]): None
#+ update(object: ObjectFileDirectory, data: Dict[str,str]): None
# + delete (object: ObjectFileDirectory, data: Dict[str,str]): None
