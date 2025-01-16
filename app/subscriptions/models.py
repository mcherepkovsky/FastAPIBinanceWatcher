import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP

from app.db.database import Base


class Subscriptions(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    pair = Column(String, nullable=False)
    interval = Column(Integer, nullable=False)
    last_sent = Column(TIMESTAMP, default=datetime.datetime.utcnow)
