from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class CreateBookingRequest(BaseModel):
    class_id: int
    client_name: str = Field(..., min_length=2)
    client_email: EmailStr


class BookingResponse(BaseModel):
    id: int
    class_id: int
    class_name: str
    start_time: datetime
    instructor: str

    model_config = {
        "from_attributes": True
    }