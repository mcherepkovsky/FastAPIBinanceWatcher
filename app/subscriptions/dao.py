from sqlalchemy import select

from app.db.dao.base import BaseDAO
from app.db.database import async_session_maker
from app.subscriptions.models import Subscriptions
from app.users.models import Users


class SubscriptionsDAO(BaseDAO):
    model = Subscriptions

    @classmethod
    async def find_all_subscriptions(cls, user_id: int):
        """
        SELECT *
        FROM bookings LEFT OUTER JOIN rooms ON rooms.id = bookings.room_id
        WHERE bookings.user_id = 1
        """
        async with async_session_maker() as session:
            query = (
                select(
                    Subscriptions.id,
                    Subscriptions.pair,
                    Subscriptions.interval
                )
                .where(Subscriptions.user_id == user_id)
            )
            result = await session.execute(query)
            return result.mappings().all()
