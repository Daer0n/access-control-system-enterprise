from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declared_attr
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable


from database.database import Base


class User(SQLAlchemyBaseUserTable[int],Base):
    __tablename__ = 'User'
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    @declared_attr
    def is_active(cls):
        return Column(Boolean, default=True, nullable=False)

    @declared_attr
    def is_superuser(cls):
        return Column(Boolean, default=False, nullable=False)

    @declared_attr
    def is_verified(cls):
        return Column(Boolean, default=False, nullable=False)
