from pydantic import BaseModel, Field
from sqlalchemy import Column, String, TEXT, INTEGER


class DataMixin(BaseModel):
    """Mixin for data format value of when the entity was created and when it was last modified. """

    language: str = Field(sa_column=Column(String, nullable=True))
    text: str = Field(sa_column=Column(TEXT, nullable=True))
    status: int = Field(sa_column=Column(INTEGER, nullable=True))
