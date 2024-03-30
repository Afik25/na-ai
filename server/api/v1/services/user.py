from datetime import datetime
from fastapi import HTTPException

from passlib.context import CryptContext

from api.v1.models import User
from api.schema import RegisterSchema, LoginSchema, ForgotPasswordSchema
from api.v1.repositories.user import UserRepository

# encrypt pssword
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Users:

    @staticmethod
    async def register(register: RegisterSchema):
        # convert birth date type from frontend str to date
        # birth_date = datetime.strftile(register.birth, '%d-%m-$Y')

        # mapping request data to class entity table
        _userObj = User(prename=register.prename, name=register.name, username=register.username,
                        password=register.password, is_completed=register.is_completed, sys_role=register.sys_role)

        # checking the username
        _username = await UserRepository.findByUsername(register.username)

        if _username:
            raise HTTPException(
                status_code=400, detail="The username already exist!")

        _userRs = await UserRepository.create(**_userObj.dict())

    @staticmethod
    async def get():
        _users = await UserRepository.getAll()

        if _users is None:
            raise HTTPException(
                status_code=400, detail={"status": 0, "length": 0, "message": "No user available!"})

        return {"status": 1, "length": len(_users), "result":  _users}

    @staticmethod
    async def onAssignationLanguage(user_id, language):
        _userMap = User(assigned_language=language)
        assign = await UserRepository.update(user_id, **_userMap.dict())

        if assign is None:
            raise HTTPException(
                status_code=400, detail={"status": 0, "length": 0, "message": "No user available!"})

        return {"status": 1, "result":  "assignation of " + language + " is done."}
