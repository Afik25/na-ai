from api.baseRepository import BaseRepository
from api.v1.models import OriginAudio, Translation
from typing import List
from sqlalchemy import update as sql_update
from sqlalchemy.future import select
from config.database import db, commit_rollback


class OriginAudioRepository(BaseRepository):
    model = OriginAudio

    @staticmethod
    async def findById(id: int):
        query = select(OriginAudio).where(OriginAudio.id == id)
        return (await db.execute(query)).scalar_one_or_none()


class TranslationRepository(BaseRepository):
    model = Translation

    @staticmethod
    async def findById(id: int):
        query = select(Translation).where(Translation.id == id)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def findByOriginId(origin_id: int):
        query = select(Translation).where(Translation.origin_id == origin_id)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def findByOriginIdAndLanguage(origin_id: int, language: str):
        query = select(Translation).where(Translation.origin_id ==
                                          origin_id, Translation.language == language)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def findByLanguage(language: str):
        query = select(Translation).where(Translation.language == language)
        return (await db.execute(query)).scalars().all()
