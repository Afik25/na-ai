from datetime import datetime, timedelta
from typing import Any, Dict, Optional
from jose import jwt
from dotenv import load_dotenv
import os
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv('.env')

ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')


class JWTRepository:
    def __init__(self, data: dict = {}, token: str = None) -> None:
        self.data = data
        self.token = token

    def generate_token(self, expires_delta: Optional[timedelta] = None):
        to_encode = self.data.copy()

        if expires_delta:
            # expire = datetime.utcnow() + expires_delta
            expire = datetime.utcnow() + timedelta(minutes=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(
            to_encode, ACCESS_TOKEN_SECRET, algorithm=ALGORITHM)

        return encode_jwt

    def decode_token(self):
        try:
            decode_token = jwt.decode(
                self.token, ACCESS_TOKEN_SECRET, algorithms=[ALGORITHM])
            return decode_token if decode_token["expires"] >= datetime.time() else None
        except:
            return {}

    @staticmethod
    def extrect_token(token: str):
        return jwt.decode(token, ACCESS_TOKEN_SECRET, algorithms=[ALGORITHM])


class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail={
                                    "status": "Forbidden", "message": "Invalid authentication schema."})
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail={
                                    "status": "Forbidden", "message": "Invalid token or expired token."})
        else:
            raise HTTPException(status_code=403, detail={
                "status": "Forbidden", "message": "Invalid authorization code."})

    @staticmethod
    def verify_jwt(jwt_token: str):
        return True if jwt.decode(jwt_token, ACCESS_TOKEN_SECRET, algorithms=[ALGORITHM]) is not None else False
