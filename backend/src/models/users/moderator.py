from sqlalchemy import Column, Integer, String
from database.database import Base
from models.users.user import User

class Moderator(User, Base):
    __tablename__ = 'Moderator'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, default='Moderator')

    def change_rights(user_id: int) -> None:
        pass