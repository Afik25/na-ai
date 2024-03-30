import os
import json
from pathlib import Path
from datetime import datetime
from secrets import token_hex
from fastapi import HTTPException
from api.v1.models import OriginAudio, Translation
from api.v1.repositories.origin import OriginRepository
from api.v1.repositories.translations import OriginAudioRepository, TranslationRepository

DATA_DIR = Path() / 'data'


class Translations:

    @staticmethod
    async def translates(user_id, origin_data, origin_audios, languages, translated_audios, translated_text):
        user_id = int(user_id[0])
        origin_data = json.loads(origin_data[0])
        newLangFolder = os.getcwd() + '/data/origins/' + origin_data['lang']

        if not os.path.exists(newLangFolder):
            os.makedirs(newLangFolder)

        newCategoryFolder = os.getcwd() + '/data/origins/' + \
            origin_data['lang'] + '/' + origin_data['category']

        if not os.path.exists(newCategoryFolder):
            os.makedirs(newCategoryFolder)

        newCategoryFile = newCategoryFolder + '/' + \
            origin_data['category'] + '-transcriptions.txt'

        if not os.path.isfile(newCategoryFile):
            f = open(newCategoryFile, 'w')
            f.close()

        counter = 0
        for i in range(len(origin_audios)):
            file_ext = origin_audios[i].filename.split(".").pop()
            current_time = datetime.now()
            file_name = f"{current_time.year}{current_time.month}{current_time.day}-{current_time.hour}{current_time.minute}{current_time.second}-{token_hex(7)}.{file_ext}"
            with open(f"{newCategoryFolder}/{file_name}", 'wb') as audioFile:
                data = await origin_audios[i].read()
                audioFile.write(data)
                with open(f"{newCategoryFile}", "a") as txtFile:
                    txtFile.write(file_name+' <---> '+origin_data['text'])
                    txtFile.write('\n')
                    _originObj = OriginAudio(
                        audio=file_name, origin_id=origin_data['id'])

                    _origRs = await OriginAudioRepository.create(**_originObj.dict())
                    if _origRs:
                        counter += 1

        for j in range(len(translated_audios)):
            newTransLangFolder = os.getcwd() + '/data/translations/' + \
                languages[j]

            if not os.path.exists(newTransLangFolder):
                os.makedirs(newTransLangFolder)

            newCategoryFolder = os.getcwd() + '/data/translations/' + \
                languages[j] + '/' + origin_data['category']

            if not os.path.exists(newCategoryFolder):
                os.makedirs(newCategoryFolder)

            newCategoryFile = newCategoryFolder + '/' + \
                languages[j] + '-' + origin_data['category'] + \
                '-transcriptions.txt'

            if not os.path.isfile(newCategoryFile):
                f = open(newCategoryFile, 'w')
                f.close()

            file_ext = translated_audios[j].filename.split(".").pop()
            current_time = datetime.now()
            file_name = f"{current_time.year}{current_time.month}{current_time.day}-{current_time.hour}{current_time.minute}{current_time.second}-{token_hex(7)}.{file_ext}"
            with open(f"{newCategoryFolder}/{file_name}", 'wb') as audioFile:
                data = await translated_audios[j].read()
                audioFile.write(data)
                with open(f"{newCategoryFile}", "a") as txtFile:
                    txtFile.write(file_name+' <---> '+translated_text[j])
                    txtFile.write('\n')

                    _transObj = Translation(
                        audio=file_name, language=languages[j], text=translated_text[j], status=1, origin_id=origin_data['id'], user_id=user_id)

                    _transRs = await TranslationRepository.create(**_transObj.dict())
                    if _transRs:
                        pass

        return {"status": 1, "message": "Data translation process done successfully!", "result":  "_transRs"}

    @staticmethod
    async def get():
        _originLanguages = await OriginRepository.getAll()
        if _originLanguages is None:
            raise HTTPException(
                status_code=400, detail={"status": 0, "length": 0, "message": "No origins data loaded yet!"})

        return {"status": 1, "length": len(_originLanguages), "result":  json.loads(_originLanguages)}
