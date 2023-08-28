from typing import List
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class TaskSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    dueDate: datetime


class RequestTask(TaskSchema):
    pass


class ResponseTask(BaseModel):
    code: str
    status: int
    response: str | TaskSchema = Field(...)


class ListResponseTask(BaseModel):
    code: str
    status: int
    response: List[TaskSchema] = Field(...)
