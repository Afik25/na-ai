from api.baseRepository import BaseRepository
from api.v1.models.User import User
from typing import List
from sqlalchemy import update as sql_update
from sqlalchemy.future import select
from config.database import db, commit_rollback


class UserRepository(BaseRepository):
    model = User

    @staticmethod
    async def findById(id: int):
        query = select(User).where(User.id == id)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def findByUsername(username: str):
        query = select(User).where(User.username == username)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def findByMail(mail: str):
        query = select(User).where(User.mail == mail)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def findByTelephone(telephone: str):
        query = select(User).where(User.telephone == telephone)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def updatePassword(mail: str, password: str):
        query = sql_update(User).where(User.mail == mail).values(
            password=password).execution_options(synchronize_session="fetch")
        await db.execute(query)
        await commit_rollback()
