from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, table
from api.v1.models.mixins import TimeMixin
from api.v1.models.data_mixins import DataMixin
from typing import List


class Origin(SQLModel, DataMixin, TimeMixin, table=True):
    __tablename__ = "origins"

    id: int = Field(primary_key=True, nullable=False)
    category: str = Field(sa_column=Column(String, nullable=True))
    audio_origin: List['OriginAudio'] = Relationship(back_populates="origin")
    translation: List['Translation'] = Relationship(back_populates="origin")
