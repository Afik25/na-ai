import uvicorn
from api.v1.controllers import authentication, user, origins, translations
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from pathlib import Path
from config.database import db
from middlewares.allowedRequestsOrigin import allowedRequestsOrigins

load_dotenv('.env')

PORT = os.getenv('PORT')
HOST = os.getenv('HOST')


def init_app():
    db.init()

    app = FastAPI(
        title="na-AI Platform",
        description="Afik Foundation Product",
        version="1"
    )

    @app.on_event("startup")
    async def starup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowedRequestsOrigins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(authentication.router)
    app.include_router(user.router)
    app.include_router(origins.router)
    app.include_router(translations.router)

    return app


app = init_app()

if __name__ == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app",
                host=HOST, port=int(PORT), reload=True)
