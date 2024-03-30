from typing import Generic, TypeVar
from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.future import select
from config.database import db, commit_rollback

T = TypeVar('T')


class BaseRepository:
    model = Generic[T]

    @classmethod
    async def create(cls, **kwargs):
        model = cls.model(**kwargs)
        db.add(model)
        await commit_rollback()
        return model

    @classmethod
    async def getAll(cls):
        query = select(cls.model)
        return (await db.execute(query)).scalars().all()

    @classmethod
    async def getByKey(cls, id: str):
        query = select(cls.model).where(cls.model.id == id)
        return (await db.execute(query)).scalars()

    @classmethod
    async def update(cls, id: int, **kwargs):
        query = sql_update(cls.model).where(
            cls.model.id == id).values(**kwargs).returning().execution_options(synchronize_session="fetch")
        await db.execute(query)
        await commit_rollback()
        return query

    @classmethod
    async def delete(cls, id: int):
        query = sql_delete(cls.model).where(cls.model.id == id)
        await db.execute(query)
        await commit_rollback()
