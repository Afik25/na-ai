from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from api.schema import ResponseSchema, CompleteRegisterSchema, CompleteActivationSchema
from middlewares.verifyJWT import JWTBearer, JWTRepository
from fastapi.security import HTTPAuthorizationCredentials
from api.v1.services.user import Users

router = APIRouter(
    prefix="/api/v1", tags=['user'], dependencies=[Depends(JWTBearer)])


class ParametersQuery(BaseModel):
    user_id: int
    language: str


@router.post("/users", response_model=ResponseSchema, response_model_exclude_none=True)
async def complete():
    pass

# @router.get("/user")
# async def get(credentials: HTTPAuthorizationCredentials):
#     token = JWTRepo().extrect_token(credentials.credentials)
#     result = await UserService.getUser(token['username'])
#     return ResponseSchema(detail="Successfully fetch data!", result=result)


@router.get("/users")
async def get():
    result = await Users.get()
    response = JSONResponse(content=jsonable_encoder(result))
    return response


@router.post("/user/assignation/language")
async def onAssignation(pq: ParametersQuery):
    result = await Users.onAssignationLanguage(pq.user_id, pq.language)
    response = JSONResponse(content=jsonable_encoder(result))
    return response
