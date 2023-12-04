from sqlalchemy import Column, Integer, String
from database.database import Base
from models.users.user import User

class DefaultUser(User, Base):
    __tablename__ = 'DefaultUser'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, default='Default user')