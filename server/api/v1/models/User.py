from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, INTEGER, BOOLEAN, table
from api.v1.models.mixins import TimeMixin
from typing import List, Optional


class User(SQLModel, TimeMixin, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True, nullable=False)
    prename: str = Field(sa_column=Column("prename", String, unique=False))
    name: str = Field(sa_column=Column("name", String, unique=False))
    gender: str = Field(sa_column=Column("gender", String, unique=False))
    telephone: str = Field(sa_column=Column("telephone", String, unique=False))
    mail: str = Field(sa_column=Column("mail", String, unique=True))
    birth: str = Field(sa_column=Column("birth", String, unique=False))
    birth_location: str = Field(sa_column=Column(
        "birth_location", String, unique=False))
    nationality: str = Field(sa_column=Column(
        "nationality", String, unique=False))
    username: str = Field(sa_column=Column("username", String, unique=True))
    password: str = Field(sa_column=Column("password", String, unique=False))
    thumbnails: str = Field(sa_column=Column(
        "thumbnails", String, unique=False))
    is_completed: bool = Field(sa_column=Column(
        "is_completed", BOOLEAN, unique=False))
    sys_role: str = Field(sa_column=Column("sys_role", String, unique=False))
    assigned_language: str = Field(sa_column=Column(
        "assigned_language", String, unique=False))
    status: int = Field(sa_column=Column("status", INTEGER, unique=False))
    #
    # relationship back_populates
    translation: List['Translation'] = Relationship(back_populates="user")

    inscription: Optional['Inscription'] = Relationship(back_populates="user")
    login: Optional['Login'] = Relationship(back_populates="user")
