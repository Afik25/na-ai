from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from dotenv import load_dotenv
import os

load_dotenv('.env')

DEV_DB_USER = os.getenv('DEV_DB_USER')
DEV_DB_PASSWORD = os.getenv('DEV_DB_PASSWORD')
DEV_DB_DATABASE_NAME = os.getenv('DEV_DB_DATABASE_NAME')

DB_CONFIG = f"postgresql+asyncpg://{DEV_DB_USER}:{DEV_DB_PASSWORD}@localhost:5432/{DEV_DB_DATABASE_NAME}"


class AsyncDatabaseSession:
    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def __getattr__(self, name: str):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(DB_CONFIG, future=True, echo=True)
        self.session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)


db = AsyncDatabaseSession()


async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
