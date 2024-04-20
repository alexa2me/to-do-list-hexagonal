from pydantic import BaseModel


class TaskModel(BaseModel):
    title: str
    description: str | None = None
    status: str
