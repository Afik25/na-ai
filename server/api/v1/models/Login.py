from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, TIMESTAMP, INTEGER, TEXT, table
from api.v1.models.mixins import TimeMixin
from typing import Optional


class Login(SQLModel, TimeMixin, table=True):
    __tablename__ = "logins"

    id: int = Field(primary_key=True, nullable=False)
    dates: datetime = Field(sa_column=Column("dates", TIMESTAMP, unique=False))
    location: str = Field(sa_column=Column("location", String, unique=False))
    latitude: str = Field(sa_column=Column("latitude", String, unique=False))
    longitude: str = Field(sa_column=Column("longitude", String, unique=False))
    device: str = Field(sa_column=Column("device", String, unique=False))
    ip_address: str = Field(sa_column=Column(
        "ip_address", String, unique=False))
    operating_system: str = Field(sa_column=Column(
        "operating_system", String, unique=False))
    navigator: str = Field(sa_column=Column("navigator", String, unique=False))
    refresh_token: str = Field(sa_column=Column(
        "refresh_token", TEXT, unique=False))
    connection_status: int = Field(sa_column=Column(
        "connection_status", INTEGER, unique=False))

    user_id: Optional[int] = Field(
        default=None, foreign_key="users.id", nullable=False)
    user: Optional["User"] = Relationship(back_populates="login")
