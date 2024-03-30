from fastapi import APIRouter, Form, Body, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from api.v1.services.translation import Translations
from typing import List

router = APIRouter(prefix="/api/v1/translate", tags=['Translations'])


@router.post("/translations")
async def translations(user_id: List[str], origin_data: List[str], languages: List[str], translated_text: List[str], origin_audios: List[UploadFile] = File(...), translated_audios: List[UploadFile] = File(...)):
    result = await Translations.translates(user_id, origin_data, origin_audios, languages, translated_audios, translated_text)
    response = JSONResponse(content=jsonable_encoder(result))
    return response
