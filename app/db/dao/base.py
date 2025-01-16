from sqlalchemy import select, insert, delete

from app.db.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = (
                insert(cls.model)
                .values(**data)
                .returning(cls.model.id, cls.model.pair, cls.model.interval)
            )
            result = await session.execute(query)
            await session.commit()
            return result.fetchone()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
