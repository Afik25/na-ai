from datetime import datetime
from fastapi import HTTPException

from passlib.context import CryptContext

from api.v1.models import User, Inscription, Login
from api.schema import RegisterSchema, CompleteRegisterSchema, CompleteActivationSchema, LoginSchema, ForgotPasswordSchema
from api.v1.repositories.user import UserRepository
from api.v1.repositories.authentication import AuthenticationRepository, LoginRepository
from middlewares.verifyJWT import JWTRepository
from utils.utils import generateCode
import os

# encrypt pssword
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Authentication:

    @staticmethod
    async def root():

        # mapping request data to class entity table
        _userObj = User(username="admin", password=pwd_context.hash(
            "admin"), is_completed=False, sys_role="admin")

        # checking the username
        _username = await UserRepository.findByUsername("admin")
        if _username:
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "The admin root already configured!"})

        _userRs = await UserRepository.create(**_userObj.dict())

        _userData = {
            "id": _userRs.id,
            "username": _userRs.username,
            "password": _userRs.password,
            "sys_role": _userRs.sys_role,
            "is_completed": _userRs.is_completed
        }

        if _userRs:
            return {"status": 1, "message": "Register successfully!", "result":  _userData}

    @staticmethod
    async def register(register: RegisterSchema):

        # mapping request data to class entity table
        _userObj = User(prename=register.prename, name=register.name, username=register.username,
                        password=pwd_context.hash(register.password), is_completed=register.is_completed, sys_role=register.sys_role)

        # checking the username
        _username = await UserRepository.findByUsername(register.username)
        if _username:
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "The username already exist!"})

        _userRs = await UserRepository.create(**_userObj.dict())

        _userData = {
            "id": _userRs.id,
            "prename": _userRs.prename,
            "name": _userRs.name,
            "username": _userRs.username,
            "password": _userRs.password,
            "sys_role": _userRs.sys_role,
            "is_completed": _userRs.is_completed
        }

        if _userRs:
            return {"status": 1, "message": "Register successfully!", "result":  _userData}

    @staticmethod
    async def complete(register: CompleteRegisterSchema):

        # checking the username
        _user = await UserRepository.findById(register.id)
        if register.username.lower() == _user.username.lower():
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "The username already exist!"})

        if not pwd_context.verify(register.old_password, _user.password):
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "Invalid old password!"})

        # mapping request data to class entity table
        usern = _user.username.lower(
        ) if register.username == '' or register.username is None else register.username
        _userObj = User(prename=register.prename, name=register.name, gender=register.gender, telephone=register.telephone,
                        mail=register.mail, birth=register.birth, birth_location=register.birth_location,
                        is_completed=register.is_completed, username=usern,
                        password=pwd_context.hash(register.new_password), status=0)

        _userRs = await UserRepository.update(register.id, **_userObj.dict())

        if _userRs is not None:
            code = generateCode(6)
            # convert birth date type from frontend str to date
            _dates = datetime.strptime(register.dates, '%Y-%m-%d %H:%M:%S')
            _inscriptionObj = Inscription(dates=_dates, code=code, location=register.location,
                                          latitude=register.latitude, longitude=register.longitude,
                                          device=register.device, ip_address=register.ip_address,
                                          operating_system=register.operating_system, navigator=register.navigator,
                                          status=0, user_id=register.id)

            _inscriptionRs = await AuthenticationRepository.create(**_inscriptionObj.dict())

            if _inscriptionRs:
                return {"status": 1, "message": "Complete Register successfully!", "code": code}

        raise HTTPException(
            status_code=400, detail={"status": 0, "message": "Complete registration failed!"})

    @staticmethod
    async def activation(register: CompleteActivationSchema):

        # checking the confirmation code
        _findInscription = await AuthenticationRepository.findByCode(register.confirmation_code)
        if _findInscription is None:
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "The confirmation code is not recognized!"})

        inscrDates = _findInscription.dates
        inscrStatus = _findInscription.status

        if inscrStatus == 1:
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "The confirmation code already used!"})

        date_format_str = '%Y-%m-%d %H:%M:%S'
        d1 = datetime.strptime(str(inscrDates), date_format_str)
        d2 = datetime.strptime(register.dates, date_format_str)

        # Get the interval in minutes
        minutes = (d2 - d1).total_seconds() / 60

        if minutes > 10:
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "The confirmation code is experired!"})

        _inscripMap = Inscription(status=1)
        inscrip = await AuthenticationRepository.update(_findInscription.id, **_inscripMap.dict())

        print({"_inscripMap ": _inscripMap, "inscrip ": inscrip})

        if inscrip is not None:
            _userMap = User(is_completed=register.is_completed)

            _actUser = await UserRepository.update(register.id, **_userMap.dict())
            print({"check _actUser ": _actUser})

            if _actUser is not None:
                return {
                    "status": 1,
                    "message": "Account confirmed and activated successfully.",
                    "result": register.confirmation_code,
                }

    @staticmethod
    async def login(login: LoginSchema):
        _username = await UserRepository.findByUsername(login.username)

        if _username is None:
            raise HTTPException(status_code=404, detail="Username not found!")

        if not pwd_context.verify(login.password, _username.password):
            raise HTTPException(
                status_code=400, detail="Invalid password!")

        refreshToken = JWTRepository(
            data={
                "userInfo": {
                    "user_id": _username.id,
                    "prename": _username.prename,
                    "name": _username.name,
                    "gender": _username.gender,
                    "telephone": _username.telephone,
                    "mail": _username.mail,
                    "birth": _username.birth,
                    "birth_location": _username.birth_location,
                    "sys_role": _username.sys_role,
                    "thumbnails": _username.thumbnails,
                    "is_completed": _username.is_completed,
                    "assigned_language": _username.assigned_language
                }
            }).generate_token()

        # convert birth date type from frontend str to date
        _dates = datetime.strptime(login.dates, '%Y-%m-%d %H:%M:%S')
        _loginObj = Login(dates=_dates, location=login.location, latitude=login.latitude,
                          longitude=login.longitude, device=login.device, ip_address=login.ip_address,
                          operating_system=login.operating_system, navigator=login.navigator,
                          refresh_token=refreshToken, connection_status=1, user_id=_username.id)

        _loginRs = await LoginRepository.create(**_loginObj.dict())

        accessToken = JWTRepository(
            data={
                "userInfo": {
                    "user_id": _username.id,
                    "prename": _username.prename,
                    "name": _username.name,
                    "gender": _username.gender,
                    "telephone": _username.telephone,
                    "mail": _username.mail,
                    "birth": _username.birth,
                    "birth_location": _username.birth_location,
                    "sys_role": _username.sys_role,
                    "thumbnails": _username.thumbnails,
                    "is_completed": _username.is_completed,
                    "assigned_language": _username.assigned_language,
                    "login": _loginRs.id
                }
            }).generate_token()

        return {"status": 1, "isLogged": True, "message": "Login successfully!", "sys_role": _username.sys_role,
                "accessToken": accessToken, "refreshToken": refreshToken}

    @staticmethod
    async def refresh(cookies: str):

        refreshToken = JWTRepository(
            data={
                "userInfo": {
                    "user_id": _username.id,
                    "prename": _username.prename,
                    "name": _username.name,
                    "gender": _username.gender,
                    "telephone": _username.telephone,
                    "mail": _username.mail,
                    "birth": _username.birth,
                    "birth_location": _username.birth_location,
                    "sys_role": _username.sys_role,
                    "thumbnails": _username.thumbnails,
                    "is_completed": _username.is_completed,
                }
            }).generate_token()

        _loginRs = await LoginRepository.findByToken(cookies)

        return {"status": 1, "isLogged": True, "message": "Login successfully!", "sys_role": "_username.sys_role",
                "accessToken": "accessToken", "refreshToken": refreshToken}

    @staticmethod
    async def forgetPassword(forget: ForgotPasswordSchema):
        _email = await UserRepository.findByMail(forget.email)

        if _email is None:
            raise HTTPException(status_code=404, detail="")
        await UserRepository.updatePassword(forget.email, pwd_context(forget.new_password))
