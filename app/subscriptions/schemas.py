from datetime import datetime

from pydantic import BaseModel


class SSubscription(BaseModel):
    id: int
    user_id: int
    pair: str
    interval: int
    last_sent: datetime = None


class NotificationData(BaseModel):
    pair: str
    interval: int
    last_sent: datetime = None
