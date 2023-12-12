from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type

from models.users.administrator import Administrator
from models.users.defaultUser import DefaultUser
from models.users.moderator import Moderator
from database.database import get_async_session

async def get_user_db(user_type: Type[DefaultUser] = DefaultUser, session: AsyncSession = Depends(get_async_session)):
    return SQLAlchemyUserDatabase(session, user_type)