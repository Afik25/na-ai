import logging
import re
from typing import Optional, TypeVar
from fastapi import HTTPException

from pydantic import BaseModel, validator

T = TypeVar('T')

# get root logger
logger = logging.getLogger(__name__)


class RegisterSchema(BaseModel):

    prename: str
    name: str
    username: str
    password: str
    is_completed: bool
    sys_role: str


class CompleteRegisterSchema(BaseModel):

    id: int
    firstname: str
    lastname: str
    gender: str
    telephone: str
    mail: str
    birth: str
    birth_location: str
    is_completed: bool
    thumbnails: Optional[str]
    nationality: str
    #
    dates: str
    location: str
    latitude: str
    longitude: str
    device: str
    ip_address: str
    operating_system: str
    navigator: str

    @validator("telephone")
    def telephone_validator(cls, v):
        logger.debug(f"phone is 2 validator: {v}")

        # regex phone number
        regex = r"^[\+]?[(]?[0-9]{4}[)]?[-\s\.]?[0-9]{4}[-\s\.]?[0-9]{1,6}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(
                status_code=400, detail={"status": 0, "message": "Invalid input phone number!"})
        return v


class CompleteActivationSchema(BaseModel):

    id: int
    dates: str
    confirmation_code: str
    is_completed: bool


class LoginSchema(BaseModel):
    username: str
    password: str
    dates: str
    location: str
    latitude: str
    longitude: str
    device: str
    ip_address: str
    operating_system: str
    navigator: str


class ForgotPasswordSchema(BaseModel):
    email: str
    new_password: str


class ResponseSchema(BaseModel):
    status: int
    message: str
    result: Optional[T] = None
