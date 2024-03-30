from datetime import datetime
from fastapi import HTTPException

from api.v1.models import Origin, OriginAudio
from api.v1.repositories.origin import OriginRepository
from api.v1.repositories.translations import OriginAudioRepository, TranslationRepository
import os


class Origins:

    @staticmethod
    async def load():

        counter = 0
        with open(os.getcwd()+"/data/clean_fr.txt", 'r') as file:
            for line in file:
                # checking the text
                _text = await OriginRepository.findByText(line)

                if _text is None:
                    # mapping request data to class entity table
                    _originObj = Origin(
                        language="fr", text=line, audio='---', status=1)

                    _origRs = await OriginRepository.create(**_originObj.dict())
                    if _origRs:
                        counter += 1

        return {"status": 1, "message": "Data process and load successfully!", "result":  counter}

    @staticmethod
    async def get(user_id, language):
        _originLanguages = await OriginRepository.getAll()
        _getAllTranslationsByLanguage = await TranslationRepository.findByLanguage(language=language)
        count_translations = 0

        for k in range(len(_getAllTranslationsByLanguage)):
            if _getAllTranslationsByLanguage[k].user_id == int(user_id):
                count_translations += 1

        if _originLanguages is None:
            raise HTTPException(
                status_code=400, detail={"status": 0, "length": 0, "message": "No origins data loaded yet!"})

        results = {}
        for i in range(len(_originLanguages)):
            currentId = _originLanguages[i].id

            _translateLanguages = await TranslationRepository.findByOriginId(currentId)

            if len(_translateLanguages) > 0:
                translates_array = []
                for j in range(len(_translateLanguages)):
                    if _translateLanguages[j].language not in translates_array:
                        translates_array.append(
                            _translateLanguages[j].language)

                if language not in translates_array:
                    results = {
                        "origin":
                        {
                            "id": _originLanguages[i].id,
                            "language": _originLanguages[i].language,
                            "category": _originLanguages[i].category,
                            "text": _originLanguages[i].text
                        },
                        "translation": translates_array,
                        "count_translations": count_translations
                    }
                    break
            else:
                results = {
                    "origin":
                    {
                        "id": _originLanguages[i].id,
                        "language": _originLanguages[i].language,
                        "category": _originLanguages[i].category,
                        "text": _originLanguages[i].text
                    },
                    "translation": [],
                    "count_translations": count_translations
                }
                break

        return {"status": 1, "length": len(results), "result":  results}
