from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from api.v1.services.origin import Origins

router = APIRouter(prefix="/api/v1/origin", tags=['Origins'])


@router.get("/load")
async def load(fileName: str, category: str):
    result = await Origins.load(fileName, category)
    response = JSONResponse(content=result)
    return response


@router.get("/get_origins_data/")
async def getAll(request: Request):
    params = request.query_params
    result = await Origins.get(params['user_id'], params['language'])
    response = JSONResponse(content=jsonable_encoder(result))
    return response
