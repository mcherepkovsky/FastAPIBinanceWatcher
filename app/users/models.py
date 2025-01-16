from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False)
    username = Column(String, nullable=True)
