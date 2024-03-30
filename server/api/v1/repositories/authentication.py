from api.baseRepository import BaseRepository
from api.v1.models.Inscription import Inscription
from api.v1.models.Login import Login
from typing import List
from sqlalchemy import update as sql_update
from sqlalchemy.future import select
from config.database import db, commit_rollback


class AuthenticationRepository(BaseRepository):
    model = Inscription

    @staticmethod
    async def findByCode(code: str):
        query = select(Inscription).where(Inscription.code == code)
        return (await db.execute(query)).scalar_one_or_none()


class LoginRepository(BaseRepository):
    model = Login

    @staticmethod
    async def findByToken(token: str):
        query = select(Inscription).where(Login.refresh_token == token)
        return (await db.execute(query)).scalar_one_or_none()
