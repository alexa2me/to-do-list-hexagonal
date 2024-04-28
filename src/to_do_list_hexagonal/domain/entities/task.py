from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


class TaskModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    title: str
    description: str | None = None
    status: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
