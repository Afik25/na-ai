from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, table
from api.v1.models.mixins import TimeMixin
from api.v1.models.data_mixins import DataMixin
from typing import Optional


class Translation(SQLModel, DataMixin, TimeMixin, table=True):
    __tablename__ = "translations"

    id: int = Field(primary_key=True, nullable=False)
    audio: str = Field(sa_column=Column(String, nullable=True))

    origin_id: Optional[int] = Field(
        default=None, foreign_key="origins.id", nullable=True)
    origin: Optional["Origin"] = Relationship(back_populates="translation")

    user_id: Optional[int] = Field(
        default=None, foreign_key="users.id", nullable=True)
    user: Optional["User"] = Relationship(back_populates="translation")
