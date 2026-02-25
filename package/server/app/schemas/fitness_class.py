from pydantic import BaseModel, Field
from datetime import datetime


class CreateClassRequest(BaseModel):
    name: str = Field(..., min_length=2)
    instructor: str = Field(..., min_length=2)
    start_time: datetime
    available_slots: int = Field(..., gt=0)


class ClassResponse(BaseModel):
    id: int
    name: str
    instructor: str
    start_time: datetime
    available_slots: int

    model_config = {
        "from_attributes": True
    }