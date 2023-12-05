from sqlalchemy import Column, Integer, String

from database.database import Base
from models.users.user import User
from models.data.data import Data

class Administrator(User, Base):
    __tablename__ = 'Administrator'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, default='Administator')

    def change_rights(user_id: int) -> None:
        pass 

    def change_role(user_id: int) -> Data:
        pass 