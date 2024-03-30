from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, table
from api.v1.models.mixins import TimeMixin
from typing import List, Optional


class OriginAudio(SQLModel, TimeMixin, table=True):
    __tablename__ = "origin_audios"

    id: int = Field(primary_key=True, nullable=False)
    audio: str = Field(sa_column=Column(String, nullable=True))

    origin_id: Optional[int] = Field(
        default=None, foreign_key="origins.id", nullable=False)
    origin: Optional["Origin"] = Relationship(back_populates="audio_origin")
