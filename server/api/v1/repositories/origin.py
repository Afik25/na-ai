from api.baseRepository import BaseRepository
from api.v1.models.Origin import Origin
from typing import List
from sqlalchemy import update as sql_update
from sqlalchemy.future import select
from config.database import db, commit_rollback


class OriginRepository(BaseRepository):
    model = Origin

    @staticmethod
    async def findById(id: int):
        query = select(Origin).where(Origin.id == id)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def findByText(text: str):
        query = select(Origin).where(Origin.text == text)
        return (await db.execute(query)).scalar_one_or_none()
