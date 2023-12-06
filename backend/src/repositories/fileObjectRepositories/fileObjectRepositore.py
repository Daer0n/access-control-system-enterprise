from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel

from models.users.user import User

class GetFileObjectRepositoreFilter(BaseModel):
    id: int | None = None
    folder_name: str | None = None

class FileObjectRepostitore:
    def __init__(self, session: AsyncSession):
        self.session = session

    def delete(file_id, user: User) -> None:
        pass
