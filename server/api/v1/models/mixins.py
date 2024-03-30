from datetime import datetime
from pydantic import BaseModel, Field
from sqlalchemy import Column, DateTime
from typing import Optional


class TimeMixin(BaseModel):
    """Mixin for datetime value of when the entity was created and when it was last modified. """

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, default=datetime.now,
                         onupdate=datetime.now, nullable=True)
    )
