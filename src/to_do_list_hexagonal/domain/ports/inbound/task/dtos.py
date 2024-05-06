from pydantic import BaseModel, Field


class CreateTaskDto(BaseModel):
    title: str = Field(examples=["Paint in watercolor"])
    description: str | None = Field(
        default=None, examples=["Practice makes improvement"]
    )
    status: str = Field(examples=["Pending"])
