from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import TIMESTAMP, Column, String, INTEGER, table
from api.v1.models.mixins import TimeMixin
from typing import Optional
from datetime import datetime


class Inscription(SQLModel, TimeMixin, table=True):
    __tablename__ = "inscriptions"

    id: int = Field(primary_key=True, nullable=False)
    dates: datetime = Field(sa_column=Column("dates", TIMESTAMP, unique=False))
    code: str = Field(sa_column=Column("code", String, unique=False))
    location: str = Field(sa_column=Column("location", String, unique=False))
    latitude: str = Field(sa_column=Column("latitude", String, unique=False))
    longitude: str = Field(sa_column=Column("longitude", String, unique=False))
    device: str = Field(sa_column=Column("device", String, unique=False))
    ip_address: str = Field(sa_column=Column(
        "ip_address", String, unique=False))
    operating_system: str = Field(sa_column=Column(
        "operating_system", String, unique=False))
    navigator: str = Field(sa_column=Column("navigator", String, unique=False))
    status: int = Field(sa_column=Column("status", INTEGER, unique=False))

    user_id: Optional[int] = Field(
        default=None, foreign_key="users.id")
    user: Optional["User"] = Relationship(back_populates="inscription")
