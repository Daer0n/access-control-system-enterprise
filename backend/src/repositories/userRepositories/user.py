
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import LargeBinary

from pydantic import BaseModel


class GetFileFilter(BaseModel):
    id: int | None = None
    file_name: str | None = None

class UserRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    def change_body() -> LargeBinary:
        pass

    def delete() -> None:
        pass