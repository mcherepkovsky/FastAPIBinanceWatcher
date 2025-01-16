import asyncio
from celery import shared_task
from app.config import settings
from aiogram import Bot
from sqlalchemy.future import select
from datetime import datetime, timedelta

from app.db.database import async_session_maker
from app.services.binance import get_currency_pair
from app.subscriptions.models import Subscriptions
from app.users.models import Users

bot = Bot(token=settings.TG_BOT_TOKEN)


@shared_task(name="process_notifications")
def process_notifications():
    # Run async code in the asyncio event loop
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(process_notifications_async())


async def process_notifications_async():
    # The original async function code here
    async with async_session_maker() as session:
        now = datetime.utcnow()
        query = select(Subscriptions)
        result = await session.execute(query)
        subscriptions = result.scalars().all()
        for sub in subscriptions:
            try:
                query = (
                    select(Users.tg_id)
                    .where(Users.id == sub.user_id)
                )
                result = await session.execute(query)
                tg_id = result.scalar()
                if sub.last_sent + timedelta(minutes=sub.interval) <= now:
                    pair_price = await get_currency_pair(sub.pair)
                    await bot.send_message(
                        chat_id=int(tg_id),
                        text=f"📢 Notification:\nPair: {sub.pair}\nPrice: {pair_price['price']}"
                    )
                    sub.last_sent = now
                    session.add(sub)
            except Exception as e:
                print(f"Failed to send notification to user {sub.user_id}: {e}")
        await session.commit()
